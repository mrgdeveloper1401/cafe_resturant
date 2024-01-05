from django.db import models
from django.urls import reverse_lazy
from core.models import Create, Update
from django.utils.translation import gettext_lazy as _
from food.managers import ActiveManager, AvailableManager
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
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'category'


class Food(Create, Update):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_food')
    food_name = models.CharField(_('نام غذا'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True, allow_unicode=True)
    food_number = models.PositiveSmallIntegerField(_('تعداد غذاهای موجود'), default=0)
    image = models.ForeignKey('images.Images', on_delete=models.PROTECT, related_name='food_images', blank=True, null=True)
    is_active = models.BooleanField(_('فعال'), default=True)
    is_get_out = models.BooleanField(_('بیرون بر'), default=True)
    pannel = models.ForeignKey('pannel.Pannel', on_delete=models.SET_NULL, related_name='pannel_food', null=True, blank=True)
    description = models.TextField(_('توضیح در مورد غذا'), blank=True, null=True)
    is_avaliable = models.BooleanField(_('غذا موجود هست'), default=True)
    buy_price = models.PositiveIntegerField(_('قیمت خرید'), default=0)
    sell_price = models.PositiveIntegerField(_('قیمت فروش'), default=0)
    discount = models.PositiveIntegerField(_('تخفیف'), default=0)
    
    objects = models.Manager()
    active = ActiveManager()
    available = AvailableManager()
    
    def get_absolute_url(self):
        return reverse_lazy("food:product_details", kwargs={"slug": self.slug})
    


    def __str__(self) -> str:
        return f'{self.food_name} -- {self.food_number} {self.sell_price}'
    
    class Meta:
        db_table = 'food'
        verbose_name = _('غذا')
        verbose_name_plural = _('غذاها')
