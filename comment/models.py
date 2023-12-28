from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update
from .managers import ActiveModel


class Comment(Create, Update):
    title_comment = models.CharField(_('عنوان'), max_length=255)
    content_comment = models.TextField(_('متن'))
    slug = models.SlugField(_('نام ��ناسه'), max_length=155, unique=True, allow_unicode=True)
    food = models.ForeignKey('food.Food', on_delete=models.PROTECT, related_name='comment_food')
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='user_comment')
    is_active = models.BooleanField(_('فعال'), default=False)
    class Ratechoose(models.TextChoices):
        one = '1', _('1')
        two = '2', _('2')
        three = '3', _('3')
        four = '4', _('4')
        five = '5', _('5')
    rate_choose = models.CharField(_('امتیاز'), max_length=5, choices=Ratechoose.choices)

    
    objects = ActiveModel()

    def __str__(self) -> str:
        return f'{self.title_comment} -- {self.user.get_full_name}'

    class Meta:
        db_table = 'comment'
        verbose_name = _('نظر')
        verbose_name_plural = _('نظرات')

    @property
    def comment_count(self):
        return Comment.objects.count()
    
class Reply(Create, Update):
    body = models.TextField(_('متن'))
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='reply_user_comment')
    food = models.ForeignKey('food.Food', on_delete=models.PROTECT, related_name='reply_comment_food')
    is_active = models.BooleanField(_('فعال'), default=False)

    objects = ActiveModel()

    def __str__(self) -> str:
        return self.body
    
    class Meta:
        db_table ='reply_comment'
        verbose_name = _('پاسخ نظر')
        verbose_name_plural = _('پاسخ نظرات')
