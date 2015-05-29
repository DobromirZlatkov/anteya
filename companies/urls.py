from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^companies/$', views.CompanyList.as_view(), name="companies", ),
    url(r'^company/$', views.CompanyCreate.as_view(), name="company_create", ),
    url(r'^company/(?P<pk>\d+)/$', views.CompanyEdit.as_view(), name="company_update", ),
    url(r'^company/(?P<pk>\d+)/delete/$', views.CompanyDelete.as_view(), name="company_delete", ),
)
