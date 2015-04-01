from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from .models import Slider


class SliderPlugin(CMSPluginBase):
    module = _("Our Mega Plugins")
    name = _("Slider Plugin")
    render_template = "slider/slider_plugin.html"
    model = Slider

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(SliderPlugin)