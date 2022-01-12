from django.conf import settings
from django.template.defaulttags import url
from django.urls import path, include
from django.conf.urls.static import static

from . import views

app_name = 'introduce'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
