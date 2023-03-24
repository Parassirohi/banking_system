from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializer import *
from .pagination import DefaultPagination
# Create your views here.


class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    pagination_class = DefaultPagination


class PublicBankViewSet(ModelViewSet):
    queryset = PublicBank.objects.all()
    serializer_class = PublicBankSerializer
    pagination_class = DefaultPagination

