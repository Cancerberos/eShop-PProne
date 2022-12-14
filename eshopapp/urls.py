from django.urls import path
from eshopapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"), 
    path('\popu', views.indexPopu, name="indexPopu"), 
    path('\promo', views.indexPromo, name="indexPromo"), 
    path('\about', views.about, name="about"), 
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
