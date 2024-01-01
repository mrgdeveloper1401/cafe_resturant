from django.db import models
from core.models import Create, Update
from django.utils.translation import gettext_lazy as _


class Contact(Create, Update):
    first_name = models.CharField(_('نام'), max_length=100)
    last_name = models.CharField(_('نام خانوادگی'), max_length=100)
    mobile_phone = models.CharField(_('شماره همراه'), max_length=11)
    email = models.EmailField(_('ایمیل'), max_length=100)
    body = models.TextField(_('متن'))
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.mobile_phone} '

    class Meta:
        db_table = 'contact'
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
