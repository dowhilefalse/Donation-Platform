from django.shortcuts import render

# Create your views here.
import re
import traceback

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.contrib.auth import login,  logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from .models import User
from api.views import OrganizationViewSet, TeamViewSet


def view_index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def view_contact(request):
    if request.method == 'POST':
        return redirect(reverse('registration:page_index'))
    context = {}
    return render(request, 'pages/contact.html', context)

def view_register(request):
    if request.method == 'POST':
        return redirect(reverse('registration:page_index'))
    context = {}
    return render(request, 'pages/register.html', context)

def view_about(request):
    if request.method == 'POST':
        return redirect(reverse('registration:page_index'))
    context = {}
    return render(request, 'pages/about.html', context)

# --------------------------------------------------------------
def view_group1(request):
    if request.method == 'POST':
        return redirect(reverse('registration:page_index'))
    context = {}
    return render(request, 'pages/group1.html', context)

def view_group11(request):
    '''
    武汉医院
    '''
    if request.method == 'POST':
        return redirect(reverse('registration:page_index'))
    # 传递查询参数, 调用API方法
     # django请求参数需要修改_mutable属性(方式一)后才能修改
    request.GET._mutable = True #to make it editable
    request.GET['scope'] = 'wuhan'
    request.GET._mutable = False #make it False once edit done
    obj = OrganizationViewSet.as_view({'get': 'list'})(request)
    print(obj.data)
    # TODO: 将obj.data传递到模板中
    context = {
        'labels': [],
        'content': [],
    }
    return render(request, 'pages/group11.html', context)

def view_group12(request):
    '''
    周边城市
    '''
    if request.method == 'POST':
        return redirect(reverse('registration:page_index'))
    # 传递查询参数, 调用API方法
    request.GET = request.GET.copy()
    request.GET['scope'] = 'hubei'
    obj = OrganizationViewSet.as_view({'get': 'list'})(request)
    print(obj.data)
    # TODO: 将obj.data传递到模板中
    context = {
        'labels': [],
        'content': [],
    }
    return render(request, 'pages/group12.html', context)

# --------------------------------------------------------------
def view_group2(request):
    '''
    全国各地
    '''
    if request.method == 'POST':
        return redirect(reverse('registration:page_index'))
    # 传递查询参数, 调用API方法
    request.GET = request.GET.copy() # django请求参数需要复制(方式二)后才能修改
    request.GET['scope'] = 'china'
    obj = OrganizationViewSet.as_view({'get': 'list'})(request)
    print(obj.data)
    # TODO: 将obj.data传递到模板中
    context = {}
    return render(request, 'pages/group2.html', context)

# --------------------------------------------------------------
def view_group3(request):
    '''
    爱心团体
    '''
    if request.method == 'POST':
        return redirect(reverse('registration:page_index'))
    obj = TeamViewSet.as_view({'get': 'list'})(request)
    print(obj.data)
    # TODO: 将obj.data传递到模板中
    context = {}
    return render(request, 'pages/group3.html', context)

# --------------------------------------------------------------
def view_registerform(request):
    req_dict = getattr(request, request.method.upper(), request.POST)
    username = req_dict.get('username', None)
    phone = req_dict.get('phone', None)
    captcha_code = req_dict.get('captcha', None)
    password1 = req_dict.get('password1', None)
    password2 = req_dict.get('password2', None)
    # 取session
    session_key = 'captcha-{0}'.format(phone)
    session_code = request.session.get(session_key, None)
    # 验证
    error = 1
    desc = '请求错误'
    code_ok = bool(captcha_code)
    if bool(session_code):
        username_ok = bool(username)
        phone_ok = bool(phone) and bool(session_code) # session存在，说明手机号有效
        code_ok = code_ok and captcha_code == session_code
        password_ok = bool(password1) and password1 == password2
        if username_ok and phone_ok and code_ok and password_ok:
            qs = User.objects.filter(phone=phone)
            if qs.exists():
                error = 2
                desc = '手机号 {0} 已注册'.format(phone)
            else:
                qs = User.objects.filter(username=username)
                if qs.exists():
                    error = 3
                    desc = '用户名 {0} 已被使用'.format(username)
                else:
                    try:
                        user = User()
                        user.username = username
                        user.phone = phone
                        user.set_password(password1)
                        user.save()
                        if user.pk is not None:
                            # 删除session中的验证码
                            del request.session[session_key]
                            error = 0
                            desc = '注册成功'
                        else:
                            error = 8
                            desc = '注册失败'
                    except Exception as e:
                        traceback.print_exc()
                        error = 6
                        desc = '注册失败'
        else:
            error = 7
            desc = '参数错误'
    else:
        if code_ok:
            error = 4
            desc = '验证码已过期'
        else:
            error = 5
            desc = '缺少参数(手机号、验证码)'
    return JsonResponse({
        'error': error,
        'desc': desc,
    })

def view_phone_captcha(request):
    req_dict = getattr(request, request.method.upper(), request.POST)
    phone = req_dict.get('phone', None)
    # 验证
    error = 1
    desc = '请求错误'
    # TODO: 验证手机号有效性
    phone_ok = bool(phone)
    if phone_ok:
        # TODO: 请求频率限制
        rate_ok = True
        if rate_ok:
            # TODO: 生成验证码
            code = '123579'
            try:
                # TODO: 发送验证码
                send_ok = True
                if send_ok:
                    session_key = 'captcha-{0}'.format(phone)
                    request.session[session_key] = code
                    error = 0
                    desc = '发送成功'
                else:
                    error = 4
                    desc = '发送失败'
            except Exception as e:
                traceback.print_exc()
                error = 5
                desc = '发送失败'
        else:
            error = 3
            desc = '验证码发送太频繁'
    else:
        error = 2
        desc = '手机号无效'
    return JsonResponse({
        'error': error,
        'desc': desc,
    })

def view_login(request):
    if request.method == 'POST':
        account = request.POST.get('account', None)
        password = request.POST.get('password', None)
        error_message = None
        if bool(account) and bool(password):
            # TODO: 数据严格格式校验
            # 查询
            queryset = User.objects.filter(Q(username=account) | Q(phone=account))
            existed_user = queryset.first()
            if existed_user is not None:
                user = authenticate(username=existed_user.username, password=password)
                if user is not None:
                    login(request, user=user)
                    return redirect(reverse('registration:page_index'))
                else:
                    # return HttpResponse('密码错误')
                    error_message = '密码错误'
            else:
                # return HttpResponse('账户不存在')
                error_message = '账户不存在'
        else:
            # return HttpResponse('缺少参数')
            error_message = '缺少参数'
        if bool(error_message):
            messages.add_message(request, messages.ERROR, error_message)
    context = {}
    return render(request, 'pages/login.html', context)

def view_logout(request):
    logout(request) # 清除session
    return redirect(reverse('registration:page_index'))
