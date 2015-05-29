from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^orders/$', views.OrderView.as_view(), name="orders", ),
   # url(r'^order/$', views.OrderView.as_view(), name="orders", ),
    #url(r'^order/(?P<pk>\d+)/$', views.OrderEdit.as_view(), name="order_update", ),
    #url(r'^order/(?P<pk>\d+)/delete/$', views.OrderDelete.as_view(), name="order_delete", ),
)
