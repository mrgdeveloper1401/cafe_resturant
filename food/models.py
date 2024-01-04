from django.db import models
from django.urls import reverse_lazy
from core.models import Create, Update
from django.utils.translation import gettext_lazy as _
from food.managers import ActiveManager, AvailableManager


class Food(Create, Update):
    category = models.ForeignKey('category.Category', on_delete=models.PROTECT, related_name='category_food')
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


# class FoodAttribute(Create, Update):
#     attribute = models.CharField(_('attribute'), max_length=100)
#     food = models.ForeignKey(Food, on_delete=models.PROTECT, related_name='food_attributes')
    
#     def __str__(self) -> str:
#         return self.attribute
    
#     class Meta:
#         db_table = 'food_attributes'
#         verbose_name = _('attribute')
#         verbose_name_plural = _('attributes')


# class FoodAttributeValues(Create, Update):
#     value = models.CharField(_('value'), max_length=100)
#     food_attribute_value_char = models.ForeignKey(FoodAttribute, on_delete=models.PROTECT, related_name='food_attribute_values')
#     food_attribute_value_int = models.PositiveIntegerField(blank=True, null=True)
#     food = models.ForeignKey(Food, on_delete=models.PROTECT, related_name='food_attribute_values')
    
#     def __str__(self) -> str:
#         return self.value
    
#     class Meta:
#         db_table = 'food_attribute_values'
#         verbose_name = _('value')
#         verbose_name_plural = _('values')