from django.conf.urls import url
from .views import index, add_surat, delete_surat
#url for app
app_name = 'message'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_surat', add_surat, name='add_surat'),
    url(r'^delete_surat/(?P<id_num>\d+)/$', delete_surat, name='delete_surat'),
]
