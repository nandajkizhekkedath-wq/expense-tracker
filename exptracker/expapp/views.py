from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from expapp.serializers import UserSerializer,ExpenseSerializer
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from expapp.models import Expense
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.

class UserRegister(CreateAPIView):
    serializer_class=UserSerializer

    def perform_create(self, serializer):
        return User.objects.create_user(**serializer.validated_data)

class ExpenseCreateList(CreateAPIView,ListAPIView):
    serializer_class=ExpenseSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        return serializer.save(owner=user)

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)

    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields=["title"]
    search_fields=["category","payement"]
    Ordering_fields=["ammount","created_at"]


class ExpenseRetrieveUpdateDestroy(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=ExpenseSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)