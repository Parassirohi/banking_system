from rest_framework import serializers

from .models import *


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ['ifsc', 'address', 'city', 'district', 'state']


class SimpleBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class PublicBankSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicBank
        fields = ['id', 'name']


class BankBranchSerializer(serializers.ModelSerializer):
    branches = SimpleBranchSerializer(many=True)

    class Meta:
        model = PublicBank
        fields = ['branches']
