#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from config import EMAIL_ARGS
from pycrypto_moudle import decrypt_method
from email.mime.text import MIMEText
from email.utils import formataddr
import re


# 发件人邮箱账号
my_sender = '2695585334@qq.com'
# user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功
my_pass = ''

def check_addr(addr):
    str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
    if re.match(str, addr):
        return True
    else:
        return False


def send_mail(receiver_addr,receiver_user,send_content):
    ret = True
    try:
        # 邮件内容
        msg = MIMEText(send_content, 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["运营工具-账号系统", my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr([receiver_user, receiver_addr])
        # 邮件的主题
        msg['Subject'] = "运营工具-账号系统-密码"

        # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
        # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
        # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.login(my_sender, my_pass)
        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, [receiver_addr, ], msg.as_string())
        # 关闭连接
        server.quit()
        # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    except Exception as e:
        print(e)
        ret = False
    return ret


