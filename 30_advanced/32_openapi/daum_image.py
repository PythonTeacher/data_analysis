# open api 사용하기
# daum : http://developers.daum.net/
# key 생성 시 웹브라우져를 선택하기
from urllib.request import urlopen, quote
import json
from pprint import pprint
import html

apiKey = "a4992c6f0f87fbd54fb7bff4a4c939e5"
q = "뽀로로"
output = "json"

url = "https://apis.daum.net/search/image?apikey={apiKey}&q={q}&output={output}"\
        .format(apiKey=apiKey, q=quote(q), output=output)

f = urlopen(url)

print(f.headers)
body = f.read()
print(body)
print(type(body))

# bytes -> str
s = body.decode("utf-8")
print(s)

s = html.unescape(s)

# str -> dict
j = json.loads(s)
print(j)
print(type(j))

pprint(j)

# item['title'], item['image']
items = j['channel']['item']
print(items)

cnt = 1
for item in items:
    print("%d. title : %s, image : %s" % (cnt, item['title'], item['image']))
    cnt += 1

html = '''
<html>
<head>
<title>Daum Open API</title>
</head>
<body>
<h1>이미지 검색 결과</h1>
<ul>
'''
for item in items:
    html += '<li>'
    html += '<p>타이틀 : ' + item['title'] + '</p>'
    html += '<img src="' + item['image'] + '" width=200>'
    html += '</li>'

html += '''
</ul>
</body>
</html>
'''

with open('daum_image.html', 'w', encoding='utf-8') as f:
    f.write(html)






