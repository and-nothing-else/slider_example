from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('cms.urls')),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
