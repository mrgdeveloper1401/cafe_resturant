from django.db import models
from core.models import Create, Update
from django.utils.translation import gettext_lazy as _


class Contact(Create, Update):
    landing_phone = models.CharField(_('شماره ثابت'), max_length=12, blank=True, null=True)
    mobile_phone = models.CharField(_('شماره همراه'), max_length=11)
    email = models.EmailField(_('ایمیل'), max_length=100)
    fax = models.CharField(_('fax'), max_length=20, blank=True, null=True)
    body = models.TextField(_('متن'))
    is_active = models.BooleanField(_('is_active'), default=True)
    
    def __str__(self) -> str:
        return f'{self.landing_phone} & {self.mobile_phone} & {self.email}'

    class Meta:
        db_table = 'contact'
        verbose_name = _('راه های ارتباطی با ما')
        verbose_name_plural = _('راه های ارتباطی با ما')


class ContactUs(Create, Update):
    email = models.EmailField(_('ایمیل'), max_length=255, blank=True, null=True)
    mobile_phone = models.CharField(_('شماره موبایل'), max_length=11, blank=True, null=True)
    description =models.TextField(_('توضحات'))
    location = models.CharField(_('محل شعبه'), max_length=255, blank=True, null=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    
    class Meta:
        db_table = 'contact_us'
        verbose_name = _('تماس با ما')
        verbose_name_plural = _('تماس با ما')