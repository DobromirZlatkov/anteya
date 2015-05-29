from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts import urls as accounts_urls
from companies import urls as companies_urls

urlpatterns = patterns(
    '',

    url(r'^', include(accounts_urls)),

    url(r'^user/(?P<id>\d+)/', include(companies_urls)),

    url(r'^admin/', include(admin.site.urls)),
)
