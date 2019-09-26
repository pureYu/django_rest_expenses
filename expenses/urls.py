from rest_framework.routers import DefaultRouter

from .views import CostViewSet


router = DefaultRouter()
router.register(r'costs', CostViewSet, basename='user')    # why 'user'????

urlpatterns = router.urls