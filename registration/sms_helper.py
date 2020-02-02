# -*- coding: utf-8 -*-
# refer: https://api.aliyun.com/?spm=a2c4g.11186623.2.17.564859adlCw1b0#/?product=Dysmsapi&api=SendSms&tab=DEMO&lang=PYTHON
import json
import traceback

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

from django.conf import settings


def send_sms(phone, code):
    '''
    发送短信
    '''
    # 读取配置
    accessKeyId = settings.SMS_accessKeyId
    accessSecret = settings.SMS_accessSecret
    TemplateCode = settings.SMS_TemplateCode
    SignName = settings.SMS_SignName
    # 阿里云短信API配置(固定参数)
    client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')
    # 阿里云短信API配置(动态参数) 
    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', SignName)
    request.add_query_param('TemplateCode', TemplateCode)
    request.add_query_param('TemplateParam', '{{"code":"{0}"}}'.format(code)) # 外层json的{}需要转义

    is_ok = False
    error_message = None
    try:
        response = client.do_action(request)
        if bool(response):
            raw_str = str(response, encoding = 'utf-8')
            resp = json.loads(raw_str, encoding='utf-8')
            if resp.get('Code', '').upper() == 'OK':
                is_ok = True
            else:
                error_message = '短信服务错误({0})'.format(resp.get('Message', ''))
    except Exception as e:
        error_message = '服务器错误({0})'.format(e)
        traceback.print_exc()
    return is_ok, error_message

if __name__ == '__main__':
    # demo (有读取django配置, 需要在django项目中使用)
    phone = ''
    code = '123579'
    if bool(phone):
        send_ok, error_message = send_sms(phone, code)
        if send_ok:
            print('发送成功')
        else:
            print('发送失败: {0}'.format(error_message))
    else:
        print('请修改代码, 填写要发送验证码的手机号(phone)')