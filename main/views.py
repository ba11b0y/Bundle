from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseForbidden
from django.db import models
from .models import User
# Create your views here.
def ping(request):
    html = "<html><body>Pong.</body></html>"
    return HttpResponse(html)
def goals(request, user):
    try:
        user_check = User.objects.get(email=user)
    except Exception as e:
        html = "<html><body>Debug:    {}</body></html>".format(e)
        return HttpResponse(html)
        #return HttpResponseForbidden
    return JsonResponse({'Data':str(user_check)})