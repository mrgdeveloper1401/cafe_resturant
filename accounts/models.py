from datetime import timedelta, timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import Create, Update
from .managers import UserManagers


class User(AbstractBaseUser, PermissionsMixin, Create, Update):
    first_name = models.CharField(_('نام'), max_length=100)
    last_name = models.CharField(_('نام خانوادگی'), max_length=100)
    email = models.EmailField(_('ایمیل'), unique=True, max_length=255, blank=True, null=True)
    mobile_phone = models.CharField(_('شماره موبایل'), max_length=11, unique=True)
    is_active = models.BooleanField(_('کاربر فعال'), default=False, editable=False)
    is_staff = models.BooleanField(_('دسترسی کارمندی'), default=False, editable=False)
    bio = models.TextField(_('درباره خودت'), blank=True, null=True)
    address = models.TextField(_('آدرس کامل'), blank=True, null=True)
    postal_code = models.CharField(_('کد پستی'), max_length=11, unique=True, null=True, blank=True)
    nation_code = models.CharField(_('کد ملی'), max_length=11, blank=True, null=True, unique=True)
    image = models.ForeignKey('images.Images', on_delete=models.PROTECT, blank=True, null=True)
    birth_day = models.DateField(_("تاریخ تولد"), blank=True, null=True)
    job = models.ManyToManyField('Job', related_name='users', blank=True)
    
    objects = UserManagers()
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "mobile_phone"
    REQUIRED_FIELDS = ("email",)
    
    
    class Meta:
        verbose_name = _("کاربر")
        verbose_name_plural = _("کاربران")
        db_table = 'user'

    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    # TODO
    @property
    def membership(self):
        expiration_date = self.create_at
        if self.is_active:
            return self.is_active and timezone.now() <= expiration_date
    



# model send code for User
class OtpCode(models.Model):
    mobile_phone = models.CharField(_('شماره موبایل'), max_length=11, unique=True)
    code = models.PositiveIntegerField()
    create_code = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.mobile_phone} - {self.code} - {self.create_code}'
    
    class Meta:
        db_table = 'otp_code'
        verbose_name = _('کد تایید')
        verbose_name_plural = _('کد تایید')


class Job(Create, Update):
    job_name = models.CharField(_('نام شغل'), max_length=150)
    
    def __str__(self) -> str:
        return self.job_name
    
    class Meta:
        db_table = 'job'
        verbose_name = _('شغل')
        verbose_name_plural = _('شغل ها')