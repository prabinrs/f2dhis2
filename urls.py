from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'f2dhis2.views.home', name='home'),
    # url(r'^f2dhis2/', include('f2dhis2.foo.urls')),

    url(r'^(?P<id_string>[^/]+)/post/(?P<id>[^/]+)$',
        'main.views.initiate_formhub_request', name='home'),
    url(r'^dataset-import$',
        'main.views.dataset_import', name='dataset-import'),
    url(r'^fh-import$',
        'main.views.formhub_import', name='fh-import'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
