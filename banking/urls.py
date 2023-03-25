from django.urls import path

from rest_framework_nested import routers
from . import views

router = routers.SimpleRouter()
router.register('banks', views.PublicBankViewSet)
router.register('branches', views.BranchViewSet)

urlpatterns = [
    path('banks/<int:bank_id>/ifsc/', views.GetBranchViewSet.as_view({'get': 'list'})),

]
urlpatterns += router.urls

