from orders.views import OrderViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'orders', OrderViewSet, basename='order')
urlpatterns = router.urls