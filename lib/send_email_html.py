#!/usr/bin/env python
# encoding:utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from config import *


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_email():
    smtp_server = u"smtp.163.com"  #发送渠道的端口
    # smtp_server = u"smtp.qq.com"
    from_addr = FROM_ADDR
    password = FROM_PSWD  #163设置的第三方授权码
    to_addr = TO_ADDR
    test_res = u"test_result_2016-06-06 17-02-13.html"
    html_data = ""

    if not test_res:    #若没有test_res文件，立即返回
        return
    with open(test_res) as fp:
        html_data = fp.read()    #把文本内容一次性读入内存
    #生成邮件
    msg = MIMEText(html_data, "html", "utf-8")
    msg["From"] = _format_addr(u"myself <%s>" % FROM_ADDR)  #_format_将后面的进行编码
    msg["To"] = _format_addr(U"admin <%s>" % TO_ADDR)
    msg["Subject"] = Header(u"测试报告", "utf-8").encode()

    #使用163邮箱发送
    server = smtplib.SMTP(smtp_server)
    server.set_debuglevel(2)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

    #使用QQ发送
    # try:
    #     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    #     s.login(from_addr, password)
    #     s.sendmail(from_addr, to_addr, msg.as_string())
    #     s.quit()
    #     print "Success"
    # except smtplib.SMTPException, e:
    #     print "Failed, %s" % e

    print "send ok "

if __name__ == "__main__":
    send_email()
    #pass