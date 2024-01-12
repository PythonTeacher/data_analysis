# open api 사용하기
# daum : http://developers.daum.net/
# key 생성 시 웹브라우져를 선택하기
from urllib.request import urlopen, quote
import json
from pprint import pprint

apiKey = "a4992c6f0f87fbd54fb7bff4a4c939e5"
q = "python"
output = "json"

# 책 검색 url로 수정
url = "https://apis.daum.net/search/book?apikey={apiKey}&q={q}&output={output}"\
        .format(apiKey=apiKey, q=quote(q), output=output)

f = urlopen(url)

print(f.headers)
body = f.read()
print(body)
print(type(body))

# bytes -> str
s = body.decode("utf-8")
print(s)

# str -> dict
j = json.loads(s)
print(j)
print(type(j))

pprint(j)

# item['title'], item['description'], item['author'], item['sale_price']
items = j['channel']['item']
print(items)

cnt = 1
for item in items:
    print("%d. 제목 : %s, 내용 : %s, 저자 : %s, 가격 : %s"
            % (cnt, item['title'], item['description'], item['author'], item['sale_price']))
    cnt += 1

html = '''
<html>
<head>
<title>Daum Open API</title>
</head>
<body>
<h1>책 검색 결과</h1>
<ul>
'''
for item in items:
    html += '<li>'
    html += '<p>제목 : ' + item['title'] + '</p>'
    html += '<p>내용 : ' + item['description'] + '</p>'
    html += '<p>저자 : ' + item['author'] + '</p>'
    html += '<p>가격 : ' + item['sale_price'] + '</p>'
    html += '<img src="' + item['cover_s_url'] + '"</img>'
    html += '</li>'

html += '''
</ul>
</body>
</html>
'''

with open('daum_book.html', 'w', encoding='utf-8') as f:
    f.write(html)






