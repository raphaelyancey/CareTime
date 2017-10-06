from django.conf.urls import url, include
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^host/(?P<host_slug>[-\w]+)/admin$', views.host_admin, name='host_admin'),
    url(r'^host/(?P<host_slug>[-\w]+)$', views.host_front, name='host_front'),
    url(r'^organization/(?P<org_slug>[-\w]+)$', views.organization, name='organization'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
