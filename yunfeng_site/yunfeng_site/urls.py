"""yunfeng_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#-*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from yunfeng_site import views
from yunfeng_site.views import hello, home_view, current_datetime, hours_ahead, test_bootstrap, ua_display_1, display_meta, display_meta_2, display_post, display_get, contact, ContactFormView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^$', home_view),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^test_bootstrap/$', test_bootstrap),
    url(r'^ua/$', ua_display_1),
    url(r'^request_meta/$', display_meta),
    url(r'^request_meta_2/$', display_meta_2),
    url(r'^display_post/$', display_post),
    url(r'^display_get/$', display_get),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.thanks),
    url(r'^contact_bootstrap/$', ContactFormView.as_view(), name="wyfang"),
]
