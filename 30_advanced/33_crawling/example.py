from bs4 import BeautifulSoup

html = """
<html><head><title>타이틀</title></head>
<body>
<p class="title">야구팀</p>
<p class="team">
<a href="doosan.html" id="link1">두산</a>
<a href="nc.html" id="link2">NC</a>
<a href="nexen.html" id="link3">넥센</a>
</p>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

# 첫번째 p 태그 얻기
print(soup.p)
print(soup.find('p'))

# 모든 p 태그 얻기
print(soup('p'))
print(soup.find_all('p'))

# p 태그 중에 class가 title인 것 얻기
print(soup.find_all('p', {'class': 'title'}))

# 속성값 얻기
print(soup.p.get('class'))
print(soup.p['class'])

# text 얻기
print(soup.p.text)
print(soup.p.string)
print(soup.p.get_text())

# team 출력
print(soup.find_all('p')[1].get('class'))

# anchor 태그 중 id가 link3인것 조회
print(soup.find('a', {'id': 'link3'}))

# 모든 anchor 태그의 href 속성값과 text값 출력
# doosan.html (두산)
# nc.html (NC)
# nexen.html (넥센)
teams = soup.find_all('a')
for team in teams:
    print(team.get('href') + ' (' + team.text + ')')



