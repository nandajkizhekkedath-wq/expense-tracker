from rest_framework import serializers
from django.contrib.auth.models import User
from expapp.models import Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=["title","amount","category","payment"]
        read_only_fields=["id","owner","created_at"]