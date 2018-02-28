from django.conf.urls import url
from .views import (
	crypto_list
)

urlpatterns = [
	url(r'^$', crypto_list, name='index'),
]
