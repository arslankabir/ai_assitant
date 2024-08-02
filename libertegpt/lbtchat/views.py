# lbtchat/views.py

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .liberte_ai import get_response_from_libertai

@csrf_exempt  # This is for development purposes only; use proper CSRF protection in production.
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')
        response_message = get_response_from_libertai(user_message)
        return JsonResponse({'response': response_message})
    return JsonResponse({'error': 'Invalid request'}, status=400)

from django.shortcuts import render

def home(request):
    return render(request, 'lbtchat/chat.html')  # Updated template path
