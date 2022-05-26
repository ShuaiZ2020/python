import requests,time,re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
a = True
count = -1
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54'
}
while a:
    count = count + 1
    print(count)
    if count % 3600 == 0:
        from_addr = '15204013961@163.com'
        password = '1031553016zs'
        to_addr = '2317709047@qq.com'

        msg = MIMEText('yunxingzhong','plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('运行中')

        smtpobj = smtplib.SMTP('smtp.163.com', 25) 
        smtpobj.login(from_addr,password)
        smtpobj.sendmail(from_addr,to_addr, msg.as_string())
        smtpobj.quit()

    time.sleep(1)
    # 咖啡厅
    response = requests.get('http://www.sywlrc.com/wap/index.php?c=part&keyword=%E5%92%96%E5%95%A1%E5%8E%85', headers = headers)
    html = response.text
    urls = re.findall('<div.*?>报名</div>', html)
    if urls:
        a = False
        from_addr = '15204013961@163.com'
        password = '1031553016zs'
        to_addr = '2317709047@qq.com'

        msg = MIMEText('kafei','plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('咖啡厅')

        smtpobj = smtplib.SMTP('smtp.163.com', 25) 
        smtpobj.login(from_addr,password)
        smtpobj.sendmail(from_addr,to_addr, msg.as_string())
        smtpobj.quit()
    # 图书馆
    response1 = requests.get('http://www.sywlrc.com/wap/index.php?c=part&keyword=%E4%B9%A6', headers = headers)
    html1 = response1.text
    urls1 = re.findall('<div.*?>报名</div>', html1)
    if urls1:
        a = False
        from_addr = '15204013961@163.com'
        password = '1031553016zs'
        to_addr = '2317709047@qq.com'

        msg = MIMEText('kafei','plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('图书馆')

        smtpobj = smtplib.SMTP('smtp.163.com', 25) 
        smtpobj.login(from_addr,password)
        smtpobj.sendmail(from_addr,to_addr, msg.as_string())
        smtpobj.quit()
    #抄写员
    response2 = requests.get('http://www.sywlrc.com/wap/index.php?c=part&keyword=%E6%8A%84%E5%86%99%E5%91%98', headers = headers)
    html2 = response2.text
    urls2 = re.findall('<div.*?>报名</div>', html2)
    if urls2:
        a = False
        from_addr = '15204013961@163.com'
        password = '1031553016zs'
        to_addr = '2317709047@qq.com'

        msg = MIMEText('kafei','plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('抄写员')

        smtpobj = smtplib.SMTP('smtp.163.com', 25) 
        smtpobj.login(from_addr,password)
        smtpobj.sendmail(from_addr,to_addr, msg.as_string())
        smtpobj.quit()
    #打字员
    response3 = requests.get('http://www.sywlrc.com/wap/index.php?c=part&keyword=%E6%89%93%E5%AD%97%E5%91%98', headers = headers)
    html3 = response3.text
    urls3 = re.findall('<div.*?>报名</div>', html3)
    if urls3:
        a = False
        from_addr = '15204013961@163.com'
        password = '1031553016zs'
        to_addr = '2317709047@qq.com'

        msg = MIMEText('kafei','plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('打字员')

        smtpobj = smtplib.SMTP('smtp.163.com', 25) 
        smtpobj.login(from_addr,password)
        smtpobj.sendmail(from_addr,to_addr, msg.as_string())
        smtpobj.quit()
    # 圆珠笔
    response4 = requests.get('http://www.sywlrc.com/wap/index.php?c=part&keyword=%E5%9C%86%E7%8F%A0%E7%AC%94', headers = headers)
    html4 = response4.text
    urls4 = re.findall('<div.*?>报名</div>', html4)
    if urls4:
        a = False
        from_addr = '15204013961@163.com'
        password = '1031553016zs'
        to_addr = '2317709047@qq.com'

        msg = MIMEText('kafei','plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('圆珠笔')

        smtpobj = smtplib.SMTP('smtp.163.com', 25) 
        smtpobj.login(from_addr,password)
        smtpobj.sendmail(from_addr,to_addr, msg.as_string())
        smtpobj.quit()
    # 奶茶
    response5 = requests.get('http://www.sywlrc.com/wap/index.php?c=part&keyword=%E5%A5%B6%E8%8C%B6', headers = headers)
    html5 = response4.text
    urls5 = re.findall('<div.*?>报名</div>', html5)
    if urls5:
        a = False
        from_addr = '15204013961@163.com'
        password = '1031553016zs'
        to_addr = '2317709047@qq.com'

        msg = MIMEText('kafei','plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('圆珠笔')

        smtpobj = smtplib.SMTP('smtp.163.com', 25) 
        smtpobj.login(from_addr,password)
        smtpobj.sendmail(from_addr,to_addr, msg.as_string())
        smtpobj.quit()
    # 助理
    response6 = requests.get('http://www.sywlrc.com/wap/index.php?c=part&keyword=%E5%A5%B6%E8%8C%B6', headers = headers)
    html6 = response6.text
    urls6 = re.findall('<div.*?>报名</div>', html6)
    if urls6:
        a = False
        from_addr = '15204013961@163.com'
        password = '1031553016zs'
        to_addr = '2317709047@qq.com'

        msg = MIMEText('kafei','plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('圆珠笔')

        smtpobj = smtplib.SMTP('smtp.163.com', 25) 
        smtpobj.login(from_addr,password)
        smtpobj.sendmail(from_addr,to_addr, msg.as_string())
        smtpobj.quit()