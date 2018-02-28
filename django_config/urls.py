# Update URLs to include Django Debug toolbar and the new index template

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django_apps.cryptoApp import views
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	# url(r'^$', TemplateView.as_view(template_name="index.html")),
	url(r'^rest-auth/', include('rest_auth.urls')),
	url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
	url(r'^api-token-auth/', obtain_jwt_token),
	url(r'^api-token-refresh/', refresh_jwt_token),
	url(r'^api-token-verify/', verify_jwt_token),

	# our urls
	url(r'^', include('django_apps.cryptoApp.urls', namespace='list')),
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^__debug__/', include(debug_toolbar.urls)),
	]
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
