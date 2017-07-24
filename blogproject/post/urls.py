from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^create/$', views.post_create, name="create"),
    url(r'^update/$', views.post_update, name="update"),
    url(r'^delete/$', views.post_delete, name="delete"),
    url(r'^list/$', views.post_list, name="list"),
    url(r'^detail/$', views.post_detail, name="detail"),
    url(r'^one/$', views.post_one, name="one"),
    url(r'^more/$', views.post_more, name="more"),
    url(r'^view/$', views.post_view, name="view"),
    url(r'^index/$', views.post_index, name="index"),
    url(r'^fourth/$', views.post_fourth, name="fourth"),
    url(r'^id/(?P<post_number>\d+)/$', views.post_id, name="id"),
    url(r'^form/$',  views.post_create, name="form")

#carrot ^ defines where URL begins and dollar sign $ where URL ends
]
