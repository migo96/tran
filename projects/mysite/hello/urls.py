from django.urls import path, include
from .views import HELLoAPI

urlpatterns = [
	path("hello/", HELLoAPI),
]