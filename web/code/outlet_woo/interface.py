from django.core.management.base import CommandError
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.translation import ugettext as _
from django_extensions.db import fields as extension_fields
from django.core.paginator import Paginator

from datetime import datetime
from decimal import Decimal
import json
import pytz
import requests
import urllib

from woocommerce import API

from reportlab.lib import colors
from reportlab.lib.pagesizes import A3
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Image

from catalog import models as ca
from creative import models as cr
from outlet_woo import models as wc

from pprint import pprint


class Utility:

    def __init__(self):
        print("--> Utility Init")

    def update_all_local_product_data():
        for shop in wc.Shop.objects.all():
            print("===== UPDATING {} =====".format(shop.name))
            api = APIInterface(shop)
            api.do_import()


class APIInterface:

    shopObj = None

    def __init__(self, sObj):
        self.shopObj = sObj
        self.max_per_page = 50  # Max is 100

    def do_import(self):

        if not self.shopObj.has_key:
            CommandError("There doesn't seem to be a key set for {}.".format(self.shopObj.name))

        if not self.shopObj.has_secret:
            CommandError(
                "There doesn't seem to be a 'consumer secret key' set for {}.".format(self.shopObj.name))

        apiData = API(
            url=self.shopObj.web_url,
            consumer_key=self.shopObj.consumer_key,
            consumer_secret=self.shopObj.consumer_secret,
            wp_api=True,
            version="wc/v1",
            timeout=20,
        )

        print("--> Making dummy request to extract headers...")
        response = apiData.get("products?per_page={}".format(self.max_per_page))
        if not response.ok:
            error = json.loads(response.content.decode('utf-8'))
            print("--> Error:")
            print("    Code: {}".format(error.code))
            print(" Message: {}".format(error.message))
            print("    Data: {}".format(error.data))
            CommandError("The API returned an error code.")

        api_total_pages = int(response.headers['X-WP-TotalPages'])
        api_total_products = int(response.headers['X-WP-Total'])

        self.shopObj.num_products = api_total_products
        self.shopObj.save()

        # If that was successful, then let's invalidate all local data, by
        # swapping the is_active flag to negative.
        for p in wc.Product.objects.filter(shop=self.shopObj):
            p.is_active = False
            p.save()

        print("--> There are {} products across {} API pages.".format(api_total_products, api_total_pages))

        for page in range(1, api_total_pages + 1):
            print("--> Requesting Page {}...".format(page))
            response = apiData.get("products?per_page={}&page={}".format(self.max_per_page, page))
            if not response.ok:
                error = json.loads(response.content.decode('utf-8'))
                print("--> Error:")
                print("    Code: {}".format(error.code))
                print(" Message: {}".format(error.message))
                print("    Data: {}".format(error.data))
                CommandError("The API returned an error code.")

            for p in json.loads(response.content.decode('utf-8')):

                # TODO Clean up the inbound data.
                # date_created = parse_datetime(p['date_created'])
                # pytz.timezone(self.shopObj.timezone).localize(datetime_created)
                # date_modified = parse_datetime(p['date_modified'])
                # pytz.timezone(self.shopObj.timezone).localize(datetime_modified)
                # date_on_sale_from = parse_datetrime(p['date_on_sale_from']
                sp, spCreated = wc.Product.objects.update_or_create(
                    code=p['id'],
                    shop=self.shopObj,
                    defaults={
                        'is_active': True,
                        'name': p['name'],
                        'slug': p['slug'],
                        'permalink': p['permalink'],
                        # 'date_created': date_created,
                        # 'date_modified': date_modified,
                        'product_type': p['type'],
                        'status': p['status'],
                        'featured': p['featured'],
                        'catalog_visibility': p['catalog_visibility'],
                        'description': p['description'],
                        'short_description': p['short_description'],
                        'sku': p['sku'],
                        'price': p['price'],
                        'regular_price': p['regular_price'],
                        'sale_price': p['sale_price'],
                        # 'date_on_sale_from': p['date_on_sale_from'],
                        # 'date_on_sale_to': p['date_on_sale_to'],
                        'price_html': p['price_html'],
                        'on_sale': p['on_sale'],
                    }
                )

                if spCreated:
                    print("Item Added: {} / {}".format(sp.code, sp.name))
                else:
                    print("Item Updated: {} / {}".format(sp.code, sp.name))

                # Load in Images

                # TODO Remove all old images.
                for i in p['images']:
                    # TODO Clean up image data
                    # date_created = parse_datetime(i['date_created'])
                    # pytz.timezone(self.shopObj.timezone).localize(datetime_created)
                    # date_modified = parse_datetime(i['date_modified'])
                    # pytz.timezone(self.shopObj.timezone).localize(datetime_modified)
                    im, imCreated = wc.ProductImage.objects.update_or_create(
                        code=i['id'],
                        product=sp,
                        defaults={
                            'name': i['name'],
                            'src': i['src'],
                            'alt': i['alt'],
                            'position': i['position'],
                            # 'date_created': date_created,
                            # 'date_modified': date_modified,
                        }
                    )
                    # if imCreated:
                    #     print("--> Image Added: {} / {}".format(im.code, im.name))
                    # else:
                    #     print("--> Image Updated: {} / {}".format(im.code, im.name))

    def push_skus(self):
        if not self.shopObj.has_key:
            CommandError("There doesn't seem to be a key set for {}.".format(self.shopObj.name))

        if not self.shopObj.has_secret:
            CommandError(
                "There doesn't seem to be a 'consumer secret key' set for {}.".format(self.shopObj.name))

        pages = Paginator(wc.Product.objects.filter(shop=self.shopObj), 50)
        print("There are {} items to update, and I'll do this in {} requests.".format(
            pages.count, pages.num_pages))

        for pg in pages.page_range:
            page = pages.page(pg)
            products = []
            for p in page:
                products.append({
                    "id": p.code,
                    "sku": p.sku,
                })
            data = {"update": products}

            apiData = API(
                url=self.shopObj.web_url,
                consumer_key=self.shopObj.consumer_key,
                consumer_secret=self.shopObj.consumer_secret,
                wp_api=True,
                version="wc/v1",
                timeout=20,
            )

            print("--> Page {} of {} -- updating {} products with current SKUs...".format(
                pg,
                pages.num_pages,
                self.shopObj.name
            ))
            response = apiData.post("products/batch", data)

            if not response.ok:
                error = json.loads(response.content.decode('utf-8'))
                print("--> Error:")
                print(error)
                # print("    Code: {}".format(error.code))
                # print(" Message: {}".format(error.message))
                # print("    Data: {}".format(error.data))
                CommandError("The API returned an error code.")
            else:
                print("--> Success!")


class Catalog:

    def __init__(self):
        print("--> Catalog Instantiated")

    def generate_pdf(self):

        width, height = A3
        p = canvas.Canvas("catalog.pdf", pagesize=A3)
        p.setTitle(_("Product Catalog"))
        # p.setAuthor()

        pageContent = {
            'name': {
                'text': "",
                'x': 36,
                'y': 1118,
                'font': "Helvetica",
                'fontsize': 28,
                'fontcolor': colors.Color(0, 0, 0, alpha=1),
            },
            'sku': {
                'text': "",
                'x': 600,
                'y': 1052,
                'font': "Helvetica-Bold",
                'fontsize': 18,
                'fontcolor': colors.Color(0, 0, 0, alpha=1),
            },
            'outlet': {
                'text': '',
                'x': 600,
                'y': 1030,
                'font': "Helvetica",
                'fontsize': 18,
                'fontcolor': colors.Color(0.5, 0.5, 0.5, alpha=1),
            },
            'price': {
                'text': "",
                'x': 600,
                'y': 1008,
                'font': "Helvetica",
                'fontsize': 18,
                'fontcolor': colors.Color(1, 0.5, 0.5, alpha=1),
            },
            'sizes': {
                'text': "",
                'x': 600,
                'y': 0,
                'font': "Helvetica",
                'fontsize': 18,
                'fontcolor': colors.Color(0, 0, 0, alpha=1),
            },
            'colors': {
                'text': "",
                'x': 600,
                'y': 0,
                'font': "Helvetica",
                'fontsize': 18,
                'fontcolor': colors.Color(0, 0, 0, alpha=1),
            },
            'footer': {
                'text': "",
                'x': 36,
                'y': 36,
                'font': "Helvetica",
                'fontsize': 10,
                'fontcolor': colors.Color(0.4, 0.4, 0.4, alpha=1),
            },
        }
        img_grid_scale = 141
        img_grid_row_start = 400
        img_grid_gutter = 16
        img_grid_num_per_row = 5
        page_number = 0

        for product in wc.Product.objects.all().order_by('shop', 'sku',):
            page_number += 1
            pageContent['sku']['text'] = str(product.sku)
            pageContent['name']['text'] = str(product.name.upper())
            pageContent['price']['text'] = str("$ {}".format(product.price))
            pageContent['outlet']['text'] = str(product.shop)
            pageContent['footer']['text'] = str(
                "Page {} / Generated {}".format(page_number, datetime.now()))

            images = wc.ProductImage.objects.filter(product=product)
            if len(images) > 0:
                p.drawImage(images[0].image.path, 36, 542, width=546, height=546)
            if len(images) > 1:
                item = 0
                for img in images[1:]:  # Ignore the first, since we've displayed it.
                    if not img.image:
                        img.download_image()
                        print("--> Downloading product image.")
                    col = item % img_grid_num_per_row
                    row = int(item / img_grid_num_per_row)
                    item += 1
                    # Calulate the x/y. Remember, origin is in the BOTTOM LEFT, so 'y' should
                    # move in a negative direction.
                    x = 36 + col * (img_grid_scale + img_grid_gutter)
                    y = img_grid_row_start - row * (img_grid_scale - img_grid_gutter)
                    p.drawImage(img.image.path, x, y, width=img_grid_scale,
                                height=img_grid_scale)

            for k, v in pageContent.items():
                p.setFont(v['font'], v['fontsize'])
                p.setFillColor(v['fontcolor'])
                p.setStrokeColor(v['fontcolor'])
                p.drawString(v['x'], v['y'], str(v['text']))

            # TODO Now display sizes and colors (needs to be implemented in the models)

            p.showPage()  # Ends this page and moves to the next.

        print("--> Save")
        p.save()  # Saves the document.
