from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class SliderConfig(AppConfig):
    name = 'slider'
    verbose_name = pgettext_lazy("app name", "Slider")