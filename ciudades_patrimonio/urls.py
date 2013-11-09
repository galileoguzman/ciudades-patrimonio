from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from blog import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'(?P<slug>[/w/-]+)/$', views.PostView.as_view(), name='post'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
