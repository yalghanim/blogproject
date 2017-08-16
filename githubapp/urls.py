from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^test/$', views.org_members, name="githubtest"),
	url(r'^branch/$', views.list_branch, name="githubbranch"),
	url(r'^theme/$', views.theme, name="theme"),
]