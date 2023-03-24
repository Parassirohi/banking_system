from rest_framework import serializers

from .models import *


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ['ifsc', 'address', 'city', 'district', 'state']


class PublicBankSerializer(serializers.ModelSerializer):
    branches = BranchSerializer

    class Meta:
        model = PublicBank
        fields = ['id', 'name', 'branches']
