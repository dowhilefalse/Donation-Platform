from django.shortcuts import render

# Create your views here.
# import charity_forms
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, reverse
import re

# from charity_forms.models import wuhan
from django.shortcuts import render
# from web import forms   
# from models import wuhan
from django.db import connection
# print(models.wuhan)


def get_donation_data(connection, form):
    cur = connection.cursor()
#     # get annual sales rank
    sql = "select * from "+form
    cur.execute(sql)
    content = list(cur.fetchall())    
    new_content = []
    for i in range(len(content)):
        if content[i][0] is None:
            content = content[:i]
            break
        else:
            new_content.append(list(content[i]))
    for i in range(len(new_content)):
        for j in range(len(new_content[i])):
            new_content[i][j] = str(new_content[i][j])
        
    # 获取表头
    sql = "SHOW FIELDS FROM quanguo"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    cur.close()   
    return labels, content
    
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
    
    labels, content = get_donation_data(connection, 'wuhan')
    context = {
        'labels': labels,
        'content': content,
    }
    return render(request, 'pages/group11.html', context)

def view_group12(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    labels, content = get_donation_data(connection, 'zhoubian')
    context = {
        'labels': labels,
        'content': content,
    }
    return render(request, 'pages/group12.html', context)

# --------------------------------------------------------------
def view_group2(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    labels, content = get_donation_data(connection, 'quanguo')
    context = {
        'labels': labels,
        'content': content,
    }
    return render(request, 'pages/group2.html', context)


def view_group3(request):
    if request.method == 'POST':
        return redirect(reverse('page_index'))
    labels, content = get_donation_data(connection, 'quanguo')
    context = {
        'labels': labels,
        'content': content,
    }
    return render(request, 'pages/group3.html', context)
