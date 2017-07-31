from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^create/$', views.post_create, name="create"),
    url(r'^delete/$', views.post_delete, name="delete"),
    url(r'^list/$', views.post_list, name="list"),
    url(r'^detail/$', views.post_detail, name="detail"),
    url(r'^one/$', views.post_one, name="one"),
    url(r'^more/$', views.post_more, name="more"),
    url(r'^view/$', views.post_view, name="view"),
    url(r'^index/$', views.post_index, name="index"),
    url(r'^fourth/$', views.post_fourth, name="fourth"),
    url(r'^id/(?P<slug>[-\w]+)/$', views.post_id, name="id"),
    url(r'^form/$',  views.post_create, name="form"),
    url(r'^update/(?P<slug>[-\w]+)/$', views.post_update, name="update"),
    url(r'^delete/(?P<slug>[-\w]+)/$', views.post_delete, name="delete"),
    url(r'^new/$', views.new_list, name="new")
 
 #[-\w] takes the minues sign & Words, + means more than one,,,,, \d+ for Digits
#carrot ^ defines where URL begins and dollar sign $ where URL ends
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)