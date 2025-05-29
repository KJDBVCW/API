from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrinkViewSet
from . import views
from django.views.generic import TemplateView
# Tạo router cho viewset
router = DefaultRouter()
router.register(r'drinks', DrinkViewSet)

# Định nghĩa các URL
urlpatterns = [
    path('add.html', views.add_item, name='add_item'),
    path('', views.home, name='home'),
    path('api/', include(router.urls)), 
]
