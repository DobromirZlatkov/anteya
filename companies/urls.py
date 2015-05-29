from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^companies/$', views.CompanyList.as_view(), name="companies", ),
    url(r'^company/$', views.CompanyCreate.as_view(), name="company_create", ),
)
