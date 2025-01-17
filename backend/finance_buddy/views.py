from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

def example_api(request):
    data = {
        "message": "Hello from Django!",
        "status": "success"
    }
    return JsonResponse(data)

def login(request):
    return render(request, 'finance_buddy/login.html')

def finances(request):
    return render(request, 'finance_buddy/dashboard.html')

def dashboard(request):
    return render(request, 'finance_buddy/finances.html')

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