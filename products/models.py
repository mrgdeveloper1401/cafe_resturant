from django.db import models
from django.urls import reverse_lazy
from core.models import Create, Update
from django.utils.translation import gettext_lazy as _
from products.managers import ActiveManager, AvailableManager
from mptt.models import MPTTModel, TreeForeignKey
from core.models import Create, Update

class Category(Create, Update, MPTTModel):
    title = models.CharField(_('عنوان'), max_length=100, db_index=True)
    slug = models.SlugField(_('اسلاگ'), allow_unicode=True, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(_('فعال'), default=True)
    image = models.ForeignKey('images.Images', on_delete=models.PROTECT, related_name='category_images', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی ها')
        db_table = 'category'


class Product(Create, Update):
    category = models.ManyToManyField(Category, related_name='product')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, related_name='product_brand', blank=True, null=True)
    product_name = models.CharField(_('نام غذا'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, allow_unicode=True)
    product_number = models.PositiveSmallIntegerField(_('تعداد کالاهای موجود'), default=0)
    image = models.ForeignKey('images.Images', on_delete=models.PROTECT, related_name='product_images', blank=True, null=True)
    is_active = models.BooleanField(_('فعال'), default=True)
    is_get_out = models.BooleanField(_('ارسال از طریق پست'), default=True)
    description = models.TextField(_('توضیح در مورد کالا'), blank=True, null=True)
    is_avaliable = models.BooleanField(_('کالا موجود هست'), default=True)
    buy_price = models.PositiveIntegerField(_('قیمت خرید'), default=0)
    sell_price = models.PositiveIntegerField(_('قیمت فروش'), default=0)
    discount = models.PositiveIntegerField(_('تخفیف'), default=0)
    type_category = models.CharField(max_length=50, blank=True, null=True, choices=[
        ('featured', 'پیشنهاد شگفت‌انگیز'),
        ('popular', 'محبوب ترین'),
        ('discounted', 'تخفیفات ویژه'),
        ('Bestselling', 'پرفروش ترین')
    ])
    
    def __str__(self) -> str:
        return self.product_name

    objects = models.Manager()
    active = ActiveManager()
    available = AvailableManager()
    
    def get_absolute_url(self):
        return reverse_lazy("product:product_details", kwargs={"slug": self.slug})
    
    class Meta:
        db_table = 'product'
        verbose_name = _('محصول')
        verbose_name_plural = _('محصولات')


class ProductAtrribute(Create, Update):
    attribute_name = models.CharField(_("ویژگی"), max_length=100)
    
    def __str__(self) -> str:
        return self.attribute_name
    
    class Meta:
        db_table = 'product_attribute'
        verbose_name = _('ویژگی')
        verbose_name_plural = _('ویژگی ها')


class ProductAttributeValue(Create, Update):
    attribute_value = models.CharField(_("مقدار ويژگی"), max_length=100)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='attribute_values')
    attribute = models.ForeignKey(ProductAtrribute, on_delete=models.PROTECT, related_name='attribute_values')
    
    def __str__(self) -> str:
        return f'{self.attribute_value} -- {self.product.product_name}'

    class Meta:
        db_table = 'product_attribute_value'
        verbose_name = _('مقدار')
        verbose_name_plural = _('مقدار ها')

class Brand(Create, Update):
    brand_name = models.CharField(_("برند"), max_length=100, db_index=True, unique=True)
    slug = models.SlugField(_("اسلاگ"), allow_unicode=True, unique=True, max_length=100)
    is_active = models.BooleanField(_('فعال'), default=True)

    def __str__(self) -> str:
        return self.brand_name
    
    class Meta:
        db_table = 'brand'
        verbose_name = _('برند')
        verbose_name_plural = _('برند ها')