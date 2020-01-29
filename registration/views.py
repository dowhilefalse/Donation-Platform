from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, reverse
import re


def view_index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def view_contact(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    context = {}
    return render(request, 'pages/contact.html', context)

def view_register(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    context = {}
    return render(request, 'pages/register.html', context)

def view_about(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    context = {}
    return render(request, 'pages/about.html', context)

# --------------------------------------------------------------
def view_group1(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    context = {}
    return render(request, 'pages/group1.html', context)

def view_group11(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    context = {
        'labels': [],
        'content': [],
    }
    return render(request, 'pages/group11.html', context)

def view_group12(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    context = {
        'labels': [],
        'content': [],
    }
    return render(request, 'pages/group12.html', context)

# --------------------------------------------------------------
def view_group2(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    context = {}
    return render(request, 'pages/group2.html', context)
