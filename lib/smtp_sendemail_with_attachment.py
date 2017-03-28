#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from config_template import *


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))

def send_email():
    smtp_server = u"smtp.163.com"
    from_addr = FROM_ADDR
    password = FROM_PSWD
    to_addr = TO_ADDR
    test_res = u"test_result_2016-06-06 17-02-13.html"
    html_data = ""

    #邮件对象
    msg = MIMEMultipart()
    msg["From"] = _format_addr(u"自动化平台 <%s>" % from_addr)
    msg["To"] = _format_addr(u"开发人员 <%s>" % to_addr)
    msg["Subject"] = Header(u"测试报告", "utf-8").encode()

    #邮件正文
    msg.attach(MIMEText(u"请看详情......", "plain", "utf-8"))

    #添加附件就是添加一个MIMEBase，从本地读取一个html文件
    with open(test_res, "rb") as f:
        #设置附件MIME的文件名，这里是html类型
        mime = MIMEBase("html", "html", filename = test_res)
        #加上必要的头信息：
        mime.add_header("Content-Disposition", "attachment", filename =test_res)
        mime.add_header("Content-ID", "<0>")
        mime.add_header("X-Attachment-Id", "0")
        #把附件内容读进来
        mime.set_payload(f.read())
        #用base64位编码
        encoders.encode_base64(mime)
        msg.attach(mime)

    server = smtplib.SMTP(smtp_server)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print "send ok"

if __name__ == "__main__":
    send_email()