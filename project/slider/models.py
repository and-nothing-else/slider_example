from django.db import models
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from sorl.thumbnail import ImageField
from django.utils.translation import ugettext_lazy as _


class Gallery(models.Model):
    name = models.CharField(_('name'), max_length=128)

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')


class Photo(models.Model):
    title = models.CharField(_('title'), max_length=128, null=True, blank=True)
    file = ImageField(_('file'), upload_to='images')
    gallery = models.ForeignKey(Gallery)

    def __str__(self):
        return u'%s' % self.title or self.file.name

    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photo')


class Slider(CMSPlugin):
    title = models.CharField(_('title'), max_length=128, null=True, blank=True)
    description = HTMLField(_('description'), null=True, blank=True)
    gallery = models.ForeignKey(Gallery, verbose_name=_('gallery'), null=True, blank=True)

    def get_title(self):
        return self.title or self.gallery.name

    def __str__(self):
        return u'%s' % self.get_title()