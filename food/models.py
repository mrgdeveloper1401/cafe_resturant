from django.db import models
from core.models import Create, Update
from django.utils.translation import gettext_lazy as _
from .managers import ActiveModel


class Food(Create, Update):
    food_name = models.CharField(_('نام غذا'), max_length=100)
    food_number = models.PositiveSmallIntegerField(_('تعداد غذاهای موجود'), default=0)
    image = models.ForeignKey('images.Images', on_delete=models.PROTECT, related_name='food_images', blank=True, null=True)
    is_active = models.BooleanField(_('فعال'), default=True)
    is_get_out = models.BooleanField(_('بیرون بر'), default=True)
    pannel = models.ForeignKey('pannel.Pannel', on_delete=models.SET_NULL, related_name='pannel_food', null=True)
    description = models.TextField(_('توضیح در مورد غذا'), blank=True, null=True)
    
    objects = ActiveModel()

    def __str__(self) -> str:
        return f'{self.food_name} -- {self.food_number}'
    
    class Meta:
        db_table = 'food'
        verbose_name = _('غذا')
        verbose_name_plural = _('غذاها')


class FoodPrice(Create, Update):
    food = models.ForeignKey(Food, on_delete=models.PROTECT, related_name='food_price')
    buy_price = models.PositiveIntegerField(_('قیمت خرید'), default=0)
    sell_price = models.PositiveIntegerField(_('قیمت فروش'), default=0)
    discount = models.PositiveIntegerField(_('تخفیف'), default=0)
    is_active = models.BooleanField(_('فعال'), default=True)
    pnnel = models.ForeignKey('pannel.Pannel', on_delete=models.SET_NULL, related_name='pannel_food_price', null=True, verbose_name=_('قیمت غذا'))
    
    objects = ActiveModel()
    
    @property
    def final_price(self):
        # محاسبه قیمت نهایی با توجه به تخفیف
        final_price = self.sell_price - (self.sell_price * (self.discount / 100))
        return final_price
    
    def __str__(self) -> str:
        return f'{self.food.food_name}, {self.buy_price}, {self.sell_price}'
    
    class Meta:
        verbose_name = _('قیمت')
        verbose_name_plural = _('قیمت ها')
        db_table = 'food_price'


