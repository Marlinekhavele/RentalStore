from books.views import BookViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'books', BookViewSet, basename='book')
urlpatterns = router.urls