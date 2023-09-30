from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register('customers', views.CustomerViewSet, basename='customers')

urlpatterns = router.urls
