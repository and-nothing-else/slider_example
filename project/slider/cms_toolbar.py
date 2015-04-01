from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.toolbar.items import Break
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from .models import Gallery


@toolbar_pool.register
class SliderToolbar(CMSToolbar):
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(
            ADMIN_MENU_IDENTIFIER
        )
        position = admin_menu.find_first(
            Break,
            identifier=ADMINISTRATION_BREAK
        ) + 1
        admin_menu.add_break('custom-break', position=position)
        slider_menu = admin_menu.get_or_create_menu(
            'slider-menu',
            _('Slider'),
            position=position
        )
        for gallery in Gallery.objects.all():
            slider_menu.add_modal_item(
                _('edit gallery %s') % gallery.name,
                reverse(u'admin:slider_gallery_change', args=[gallery.id])
            )
        slider_menu.add_break('custom-break')
        slider_menu.add_modal_item(
            _('add gallery'),
            reverse(u'admin:slider_gallery_add')
        )