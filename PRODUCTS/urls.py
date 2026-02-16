from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = router.urls