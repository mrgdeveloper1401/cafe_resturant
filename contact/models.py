from django.db import models
from core.models import Create, Update
from django.utils.translation import gettext_lazy as _


class WaysofCommunication(Create, Update):
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
    first_name = models.CharField(_('نام'), max_length=100)
    last_name = models.CharField(_("نام خانوادگی"), max_length=100)
    mobile_phone = models.CharField(_("شماره همراه"), max_length=11, blank=True, null=True)
    email = models.EmailField(_("ایمیل"), max_length=100)
    body = models.TextField(_("متن"))
    be_answered = models.BooleanField(_('پاسخ به صورت پیامک به من اعلام شود'), default=False)
    
    class Meta:
        db_table = 'contact_us'
        verbose_name = _('تماس با ما')
        verbose_name_plural = _('تماس با ما')