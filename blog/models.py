from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, SoftDelete, Update


class Authore(Create, Update):
    name = models.CharField(_('name'), max_length=255)
    user = models.OneToOneField('accounts.users', on_delete=models.PROTECT, related_name='authore')

    def __str__(self) -> str:
        return f'{self.name} {self.user}'

class Post(Create, Update):
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, allow_unicode=True)
    text = models.TextField(_('text'))
    image = models.ManyToManyField('images.Images')
    author = models.ForeignKey(Authore, on_delete=models.PROTECT, related_name='author')
    is_active = models.BooleanField(_('is active'), default=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table = 'posts'


class Comment(Create, Update):
    user = models.ForeignKey('accounts.users', on_delete=models.PROTECT, related_name='comment_post')
    title = models.CharField(_('title'), max_length=255)
    text = models.TextField(_('text'))
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        db_table = 'comments'

    