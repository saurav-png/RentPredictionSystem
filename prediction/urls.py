from django.urls import path
from . import views

# for static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='prediction-home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)