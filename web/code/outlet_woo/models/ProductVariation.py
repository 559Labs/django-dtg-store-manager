import uuid
import requests
import urllib
import os
import tempfile
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files
from creative import models as cr
from catalog import models as ca
from outlet_woo import models as wc


class ProductVariation(models.Model):
    TAXSTATUS_TAXABLE = 'taxable'
    TAXSTATUS_SHIPPING = 'shipping'
    TAXSTATUS_NONE = 'none'
    TAXSTATUS_CHOICES = (
        (TAXSTATUS_TAXABLE, _("Taxable")),
        (TAXSTATUS_SHIPPING, _("Shipping Only")),
        (TAXSTATUS_NONE, _("None")),
    )
    BACKORDERS_NO = 'no'
    BACKORDERS_NOTIFY = 'notify'
    BACKORDERS_YES = 'yes'
    BACKORDERS_CHOICES = (
        (BACKORDERS_NO, _("Do Not Allow")),
        (BACKORDERS_NOTIFY, _("Allow, But Notify Customer")),
        (BACKORDERS_YES, _("Allow")),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), help_text=_(""), max_length=16,
                            default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    product = models.ForeignKey(wc.Product, blank=True, null=True)
    app_added = models.DateTimeField(auto_now_add=True, help_text=_(""))
    app_last_sync = models.DateTimeField(auto_now=True, help_text=_(""))
    date_created = models.DateTimeField(_("Created"), help_text=_(
        "READONLY. The date the product was created. In the site's timezone."), blank=True, null=True)
    date_modified = models.DateTimeField(_("Modified"), help_text=_(
        "READONLY. The date the product was last modified, in the site's timezone."), blank=True, null=True)

    permalink = models.CharField(_("Permalink"), help_text=_(
        "READONLY. Product URL."), max_length=255, default="", blank=True, null=True)

    sku = models.CharField(_("SKU"), help_text=_("Unique identifier."), max_length=255,
                           default="", blank=True, null=True)

    price = models.CharField(_("Price"), help_text=_(
        "READONLY. Current product price. This is set from regular_price and sale_price."), max_length=255, default="", blank=True, null=True)
    regular_price = models.CharField(_("Regular Price"), help_text=_("Product regular price."), max_length=255,
                                     default="", blank=True, null=True)
    sale_price = models.CharField(_("Sale Price"), help_text=_("Product sale price."), max_length=255,
                                  default="", blank=True, null=True)
    date_on_sale_from = models.DateField(_("On Sale From"), help_text=_(
        "Start date of sale price. Date in the YYYY-MM-DD format."), blank=True, null=True)
    date_on_sale_to = models.DateField(_("On Sale To"), help_text=_(
        "End date of sale price. Date in the YYYY-MM-DD format."), blank=True, null=True)
    on_sale = models.BooleanField(_("On Sale?"), help_text=_(
        "READONLY. Shows if the product is on sale."), default=False)
    purchasable = models.BooleanField(_("Purchasable?"), help_text=_(
        "READONLY. Shows if the product can be bought."), default=True)

    virtual = models.BooleanField(_("Virtual?"), help_text=_(
        "If the product is virtual. Virtual products are intangible and aren’t shipped. Default is false."), default=False)
    downloadable = models.BooleanField(_("Downloadable?"), help_text=_(
        "If the product is downloadable. Downloadable products give access to a file upon purchase. Default is false."), default=False)
    download_limit = models.IntegerField(_("Download Limit"), help_text=_(
        "Amount of times the product can be downloaded, the -1 values means unlimited re-downloads. Default is -1."), default=-1)
    download_expiry = models.IntegerField(_("Download Expiry"), help_text=_(
        "Number of days that the customer has up to be able to download the product, the -1 means that downloads never expires. Default is -1."), default=-1)

    tax_status = models.CharField(_("Tax Status"), help_text=_("Tax status. Default is taxable. Options: taxable, shipping (Shipping only) and none."), max_length=15,
                                  default=TAXSTATUS_TAXABLE, choices=TAXSTATUS_CHOICES)
    tax_class = models.CharField(_("Tax Class"), help_text=_(
        "The tax class."), max_length=255, default="", null=True, blank=True)

    manage_stock = models.BooleanField(_("Manage Stock"), help_text=_(
        "Stock management at product level. Default is false."), default=False)
    stock_quantity = models.IntegerField(_("Stock Quantity"), help_text=_(
        "Stock quantity. If is a variable product this value will be used to control stock for all variations, unless you define stock at variation level."), default=0)
    in_stock = models.BooleanField(_("In Stock?"), help_text=_(
        "Controls whether or not the product is listed as “in stock” or “out of stock” on the frontend. Default is true."), default=True)
    backorders = models.CharField(_("Backorders"), help_text=_("If managing stock, this controls if backorders are allowed. If enabled, stock quantity can go below 0. Default is no. Options are: no (Do not allow), notify (Allow, but notify customer), and yes (Allow)."), max_length=255,
                                  default=BACKORDERS_NO, choices=BACKORDERS_CHOICES)
    backorders_allowed = models.BooleanField(
        _("Backorders Allowed?"), help_text=_("READONLY. Shows if backorders are allowed."), default=False)
    backordered = models.BooleanField(_("Backordered?"), help_text=_(
        "READONLY. Shows if a product is on backorder (if the product have the stock_quantity negative)."), default=False)

    weight = models.DecimalField(_("Weight"), help_text=_("Product weight in decimal format."), max_digits=10, decimal_places=2,
                                 default=0)

    # dimensions
    # shipping_class
    # shipping_class_id

    # image
    # attributes

    # FIXME This is a short-term fix. Rather than go down the attribute object
    # path, for now, we're just capturing color and size where available.
    att_color = models.CharField(_("Color"), max_length=64, null=True, blank=True, default="")
    att_color_obj = models.ForeignKey(ca.Color, null=True)
    att_size = models.CharField(_("Size"), max_length=64, null=True, blank=True, default="")
    att_size_obj = models.ForeignKey(ca.Size, null=True)

    def update_sku(self):
        # SKU should be:
        # [SERIES][DESIGN]-[SITE][ITEM]-[VARIANTCOLOR][VARIANTSIZE]
        r = [
            self.product.sku,
            "-",
            self.att_color_obj.code if self.att_color_obj else "",
            self.att_size_obj.code if self.att_size_obj else "",
        ]
        self.sku = "".join(r).upper()

    def update_meta(self):
        print("Updating: {}".format(self))
        if self.att_color:
            obj, created = ca.Color.objects.update_or_create(
                name=self.att_color,
                brand=self.product.item.brand,
                defaults={}
            )
            self.att_color_obj = obj
            if created:
                print("-- Color: Created {}".format(self.att_color_obj))
            else:
                print("-- Color: Matched {} to {}".format(self.att_color, self.att_color_obj))

        if self.att_size:
            obj, created = ca.Size.objects.update_or_create(
                name=self.att_size,
                defaults={}
            )
            self.att_size_obj = obj
            if created:
                print("-- Size: Created {}".format(self.att_size_obj))
            else:
                print("-- Size: Matched {} to {}".format(self.att_size, self.att_size_obj))

        self.save()

    def save(self, *args, **kwargs):
        self.update_sku()
        super(ProductVariation, self).save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        if self.code:
            return "{}".format(self.code)
        return _("Unnamed Product Variation")

    class Meta:
        verbose_name = _("Product Variation")
        verbose_name_plural = _("Product Variations")
        ordering = ["name", "code", ]
