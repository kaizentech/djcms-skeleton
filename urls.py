from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),  # zinnia URLS
    url(r'^comments/', include('django_comments.urls')),  # django comments URLS
]

# Change to whatever you like
admin.site.site_title = '{{ project_name }} Administration'
admin.site.index_title = '{{ project_name }} Administration'
admin.site.site_header = '{{ project_name }} Administration'
