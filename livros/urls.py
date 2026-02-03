from rest_framework.routers import DefaultRouter
from .views import LivroView

router = DefaultRouter()
router.register(r'', LivroView, basename="livro")

urlpatterns = router.urls