# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import User

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login_page(request):
    return render(request, 'blog/login_page.html')


def login(request):
    name = request.POST.get('username')
    password = request.POST.get('password')
    check_pass = User.objects.get(name=name).password
    if password == check_pass:
        # return render(request, 'blog/welcome.html')
        return HttpResponse('OK')
    else:
        return HttpResponse(check_pass + ' ' + password)
