from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

def naver_webtoon():
    html = urlopen('http://comic.naver.com/index.nhn')
    soup = BeautifulSoup(html, "html.parser")
    print(soup.prettify())

    ol = soup.find('ol', {'id': 'realTimeRankFavorite'})
    items = ol.find_all('a')
    print(items)

    rank = 1
    for item in items:
        print("%d. %s" % (rank, item.text))
        rank += 1

# 반복 수행하기
while(True):
    naver_webtoon()
    time.sleep(3)





