from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('banks', views.PublicBankViewSet)
router.register('branches', views.BranchViewSet)

urlpatterns = router.urls

