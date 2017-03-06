import django_tables2 as tables
from .models import *
from django_tables2.utils import A
from django.utils.translation import ugettext_lazy as _


class bzBrandTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_bzbrand_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_bzbrand_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = bzBrand
        sequence = ('actions', 'code', 'name', 'vendor', 'outlet')
        exclude = ('date_added', 'date_updated', 'id')
        attrs = {'class': 'table table-striped table-hover'}


class bzCreativeCollectionTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_bzbrand_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_bzbrand_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = bzCreativeCollection
        sequence = ('actions', 'code', 'name', 'bzbrand',)
        exclude = ('date_added', 'date_updated', 'id',)
        attrs = {'class': 'table table-striped table-hover'}


class bzCreativeDesignTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:app_creative_design_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:app_creative_design_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    product_count = tables.TemplateColumn("{{ record.num_products }}")

    class Meta:
        model = bzCreativeDesign
        sequence = ('actions', 'code', 'name', 'product_count', 'date_added',
                    'date_updated',)
        exclude = ('id', 'bzcreativecollection',)
        attrs = {'class': 'table table-striped table-hover'}
        empty_text = "No Designs Found."


class bzCreativeLayoutTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:app_creative_layout_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:app_creative_layout_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    product_count = tables.TemplateColumn("{{ record.num_products }}")

    class Meta:
        model = bzCreativeLayout
        sequence = ('actions', 'code', 'name', 'product_count',
                    'date_added', 'date_updated',)
        exclude = ('id', 'bzcreativecollection',)
        attrs = {'class': 'table table-striped table-hover'}
        empty_text = "No Layouts Found."


class bzCreativeRenderingTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_bzbrand_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_bzbrand_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = bzCreativeRendering
        attrs = {'class': 'table table-striped table-hover'}


class bzProductTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_bzbrand_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_bzbrand_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = bzProduct
        attrs = {'class': 'table table-striped table-hover'}


class bzProductVariantTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_bzbrand_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_bzbrand_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = bzProductVariant
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogColorTable(tables.Table):

    class Meta:
        model = pfCatalogColor
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogFileSpecTable(tables.Table):

    class Meta:
        model = pfCatalogFileSpec
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogFileTypeTable(tables.Table):

    class Meta:
        model = pfCatalogFileType
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogOptionTypeTable(tables.Table):

    class Meta:
        model = pfCatalogOptionType
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogProductTable(tables.Table):

    class Meta:
        model = pfCatalogProduct
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogSizeTable(tables.Table):

    class Meta:
        model = pfCatalogSize
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogVariantTable(tables.Table):

    class Meta:
        model = pfCatalogVariant
        attrs = {'class': 'table table-striped table-hover'}


class pfCountryTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_pfcountry_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_pfcountry_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    num_states = tables.Column(A('num_states'))

    class Meta:
        model = pfCountry
        sequence = ('actions', 'code', 'name', 'num_states')
        exclude = ('date_added', 'date_updated', 'id')
        attrs = {'class': 'table table-striped table-hover'}


class pfPrintFileTable(tables.Table):

    class Meta:
        model = pfPrintFile
        attrs = {'class': 'table table-striped table-hover'}


class pfStateTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_pfstate_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_pfstate_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = pfState
        sequence = ('actions', 'code', 'name', 'pfcountry',)
        exclude = ('date_added', 'date_updated', 'id')
        attrs = {'class': 'table table-striped table-hover'}


class pfStoreTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_pfstore_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_pfstore_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    has_auth = tables.columns.BooleanColumn(A('has_auth'))

    class Meta:
        model = pfStore
        sequence = ('actions', 'has_auth', 'code', 'name', 'website', )
        exclude = ('date_added', 'date_updated', 'id',
                   'consumer_key', 'consumer_secret',)
        attrs = {'class': 'table table-striped table-hover'}


class pfSyncItemOptionTable(tables.Table):

    class Meta:
        model = pfSyncItemOption
        attrs = {'class': 'table table-striped table-hover'}


class pfSyncProductTable(tables.Table):

    class Meta:
        model = pfSyncProduct
        attrs = {'class': 'table table-striped table-hover'}


class pfSyncVariantTable(tables.Table):

    class Meta:
        model = pfSyncVariant
        attrs = {'class': 'table table-striped table-hover'}


class wooAttributeTable(tables.Table):

    class Meta:
        model = wooAttribute
        attrs = {'class': 'table table-striped table-hover'}


class wooCategoryTable(tables.Table):

    class Meta:
        model = wooCategory
        attrs = {'class': 'table table-striped table-hover'}


class wooImageTable(tables.Table):

    class Meta:
        model = wooImage
        attrs = {'class': 'table table-striped table-hover'}


class wooProductTable(tables.Table):

    class Meta:
        model = wooProduct
        attrs = {'class': 'table table-striped table-hover'}


class wooShippingClassTable(tables.Table):

    class Meta:
        model = wooShippingClass
        attrs = {'class': 'table table-striped table-hover'}


class wooStoreTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_woostore_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_woostore_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = wooStore
        sequence = ('actions', 'code', 'base_url',
                    'consumer_secret', 'verify_ssl', 'timezone')
        exclude = ('date_added', 'date_updated', 'id')
        attrs = {'class': 'table table-striped table-hover'}


class wooTagTable(tables.Table):

    class Meta:
        model = wooTag
        attrs = {'class': 'table table-striped table-hover'}


class wooTermTable(tables.Table):

    class Meta:
        model = wooTerm
        attrs = {'class': 'table table-striped table-hover'}


class wooVariantTable(tables.Table):

    class Meta:
        model = wooVariant
        attrs = {'class': 'table table-striped table-hover'}


class wpMediaTable(tables.Table):

    class Meta:
        model = wpMedia
        attrs = {'class': 'table table-striped table-hover'}


class wpMediaSizeTable(tables.Table):

    class Meta:
        model = wpMediaSize
        attrs = {'class': 'table table-striped table-hover'}
