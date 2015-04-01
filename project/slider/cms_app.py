from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class SliderApp(CMSApp):
    name = _("Slider App")

apphook_pool.register(SliderApp)