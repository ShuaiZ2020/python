import requests
import re
import time
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54'
}
response = requests.get('http://www.2717.com/ent/meinvtupian/2019/316099.html', headers = headers)
print(response.request.headers)
html = response.text
urls = re.findall(' title=".*?"><img src="(.*?)"', html)
print(urls)
print(urls)
#urls.remove('//gravatar.loli.net/avatar/049fafbec1976dde9a7c69104dd2a959?s=40&amp;d=https%3A%2F%2Fwww.vmgirls.com%2Fimage%2F2019%2F04%2F2019-04-17_02-08-29_144.jpg&amp;r=g')
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    response = requests.get(url, headers = headers)
    with open(file_name,'wb') as f:
        f.write(response.content)