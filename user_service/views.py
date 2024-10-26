# user_service/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import User

def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return JsonResponse({'id': user.id, 'name': user.name})
