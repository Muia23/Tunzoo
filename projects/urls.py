from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/profile/', views.home, name='logged_in'),
    url(r'details/(\d)', views.details, name='details'),
    url(r'^kura/(\d)', views.kura, name='kura'),
    url(r'^newpost/', views.new_post, name='newpost'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)