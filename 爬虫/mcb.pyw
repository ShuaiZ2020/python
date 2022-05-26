import smtplib
from email.mime.text import MIMEText
from email.header import Header


from_addr = '15204013961@163.com'
password = '1031553016zs'
to_addr = '2317709047@qq.com'

msg = MIMEText('send by python','plain','utf-8')
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('python test')

smtpobj = smtplib.SMTP('smtp.163.com', 25) 
smtpobj.login(from_addr,password)
smtpobj.sendmail(from_addr,to_addr, msg.as_string())
smtpobj.quit()
