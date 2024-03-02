from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import CareersViewSet


router = SimpleRouter()
router.register('careers', CareersViewSet)

urlpatterns = router.urls

