from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^orders/$', views.OrderList.as_view(), name="orders_list", ),
    url(r'^order/create$', views.OrderView.as_view(), name="order_create", ),
    url(r'^order/(?P<pk>\d+)/$', views.OrderDetails.as_view(), name="order_details",),
    url(r'^order/(?P<pk>\d+)/edit/$', views.OrderEdit.as_view(), name="order_update",),
    #url(r'^order/(?P<pk>\d+)/$', views.OrderEdit.as_view(), name="order_update", ),
    #url(r'^order/(?P<pk>\d+)/delete/$', views.OrderDelete.as_view(), name="order_delete", ),
)
