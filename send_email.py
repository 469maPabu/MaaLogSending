# send_email.py

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(smtp_server, port, sender, password, receiver, subject, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = Header(sender)
    msg['To'] = Header(receiver)
    msg['Subject'] = Header(subject)

    try:
        if port == 465:
            server = smtplib.SMTP_SSL(smtp_server, port)
        else:
            server = smtplib.SMTP(smtp_server, port)
        server.login(sender, password)
        server.sendmail(sender, [receiver], msg.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败', e)
    finally:
        if server:
            server.quit()

