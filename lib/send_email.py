#!/usr/bin/env python
# encoding:utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(Header(name, "utf-8").encode(), addr)

def send_email():
    from_addr = u"15919760570@163.com"
    password = u""  #163设置的第三方授权码
    to_addr = u"771490249@qq.com"
    smtp_server = u"smtp.qq.com"

    msg = MIMEText(u"hello kitty", "plain", "utf-8")
    msg["From"] = _format_addr(u"myself <%s>" % from_addr)
    msg["To"] = _format_addr(U"admin <%s>" % to_addr)
    msg["Subject"] = Header(u"The greeting from SMPT", "utf-8").encode()

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(from_addr, password)
        s.sendmail(from_addr, to_addr, msg.as_string())
        s.quit()
        print "Success"
    except smtplib.SMTPException, e:
        print "Failed, %s" % e

    print "send ok "

if __name__ == __main__:
    send_email()
