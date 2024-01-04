from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update


class Sciol(Create, Update):
    sciol_name = models.CharField(_('نام شبکه مجازی'), max_length=155)
    is_active = models.BooleanField(_('فعال'), default=True)

    def __str__(self) -> str:
        return self.sciol_name
    
    class Meta:
        db_table ='sciol'
        verbose_name = _('sciol')
        verbose_name_plural = _('sciols')

class SciolValues(Create, Update):
    sciol = models.ForeignKey(Sciol, on_delete=models.PROTECT, related_name='sciol_values')
    pannel = models.ForeignKey('Pannel', on_delete=models.PROTECT, related_name='contact_pannel_values')
    value = models.URLField(_('ادرس'), max_length=255)
    description = models.TextField(_('توضیح'), blank=True, null=True)
    is_active = models.BooleanField(_('فعال'), default=True)

    # objects = ActiveModel()

    def __str__(self) -> str:
        return self.value
    
    class Meta:
        db_table ='sciol_values'
        verbose_name = _('sciol_value')
        verbose_name_plural = _('sciol values')


class Pannel(Create, Update):
    user = models.OneToOneField('accounts.Users', on_delete=models.PROTECT, related_name='user_pannel')
    is_active = models.BooleanField(_("فعال"), default=True)
    pannel_name = models.CharField(_('نام پنل'), max_length=255, unique=True)
    
    def __str__(self) -> str:
        return f'{self.user.get_full_name} -- {self.user.email}'