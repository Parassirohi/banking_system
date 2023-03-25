from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .pagination import DefaultPagination


class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    pagination_class = DefaultPagination


class PublicBankViewSet(ModelViewSet):
    queryset = PublicBank.objects.prefetch_related('branches').all()
    serializer_class = PublicBankSerializer
    pagination_class = DefaultPagination


class GetBranchViewSet(ModelViewSet):
    serializer_class = SimpleBranchSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        print(self.kwargs)
        return Branch.objects.filter(bank_id=self.kwargs['bank_id'])



