#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from .forms import LoginForm,FindpaswdForm,NewaccountForm


def index(request):
    return HttpResponse('hello world')


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form, }))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('index.html', RequestContext(request))
            else:
                return render_to_response('login.html', RequestContext(request, {'form': form, 'password_is_wrong': True}))
        else:
            return render_to_response('login.html', RequestContext(request, {'form': form, }))


def findpaswd(request):
    if request.method == 'GET':
        form = FindpaswdForm()
        return render_to_response('findpaswd.html', RequestContext(request, {'form': form, }))
    else:
        form = FindpaswdForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            mailaddress = request.POST.get('mailaddress', '')
            newpassword = request.POST.get('newpassword', '')
            user = auth.authenticate(username=username, mailaddress=mailaddress)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('index.html', RequestContext(request))
            else:
                return render_to_response('findpaswd.html', RequestContext(request, {'form': form, 'mailaddress_is_wrong': True}))
        else:
            return render_to_response('findpaswd.html', RequestContext(request, {'form': form, }))  


def newaccount(request):
    if request.method == 'GET':
        form = NewaccountForm()
        return render_to_response('newaccount.html', RequestContext(request, {'form': form, }))
    else:
        form = NewaccountForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            setmailaddress = request.POST.get('setmailaddress', '')
            setpassword = request.POST.get('setpassword', '')
            user = auth.authenticate(username=username, mailaddress=setmailaddress)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('index.html', RequestContext(request))
            else:
                return render_to_response('newaccount.html', RequestContext(request, {'form': form, 'setmailaddress_is_wrong': True}))
        else:
            return render_to_response('newaccount.html', RequestContext(request, {'form': form, }))  

    # Create your views here.
