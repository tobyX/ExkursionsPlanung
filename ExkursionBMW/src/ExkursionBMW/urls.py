from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from studenten.views import AnmeldeFormPreview, AnmeldeForm
from settings import STATIC_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', AnmeldeFormPreview(AnmeldeForm)),
    url(r'^liste', 'exkursionen.views.liste', name='Teilnehmerliste'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': STATIC_ROOT,
        }),
)
