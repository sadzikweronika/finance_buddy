from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import ExpenseSerializer


def example_api(request):
    data = {
        "message": "Hello from Django!",
        "status": "success"
    }
    return JsonResponse(data)

def login(request):
    return render(request, 'finance_buddy/login.html')

def finances(request):
    return render(request, 'finance_buddy/finances.html')

def dashboard(request):
    return render(request, 'finance_buddy/dashboard.html')

def expense_detail(request, expense_id):
    # Tu symulujemy dane; normalnie pobierane z bazy danych
    data = {
        "expense_id": expense_id,
        "name": "Groceries at Lidl",
        "amount": -60,
        "category": "Groceries",
    }
    return JsonResponse(data)

def user_profile(request, user_id):
    # Symulacja danych użytkownika
    data = {
        "user_id": user_id,
        "name": "Weronika Sadzik",
        "email": "weronika@example.com",
    }
    return JsonResponse(data)

class ExpenseListCreateAPIView(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            expense = Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return Response({"error": "Expense not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            expense = Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return Response({"error": "Expense not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            expense = Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return Response({"error": "Expense not found"}, status=status.HTTP_404_NOT_FOUND)

        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
