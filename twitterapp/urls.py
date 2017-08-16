from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^test/$', views.twitter_test, name="twittertest"),
]