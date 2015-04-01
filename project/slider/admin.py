from django.contrib import admin
from .models import Gallery, Photo
from sorl.thumbnail.admin import AdminInlineImageMixin


class PhotoInline(AdminInlineImageMixin, admin.TabularInline):
    model = Photo


class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Gallery, GalleryAdmin)