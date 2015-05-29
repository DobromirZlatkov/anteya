from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.SignInAndSignUp.as_view(), name='home'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^accounts/logout$', views.LogoutView.as_view(), name='logout'),
)
