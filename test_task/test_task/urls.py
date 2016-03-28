from django.conf.urls import include, url
from django.contrib import admin
from main.views import *

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/$', list_or_add_domains, name="domains"),
	url(r'^api/(?P<pk>\d+)/$', detail_domain),
]