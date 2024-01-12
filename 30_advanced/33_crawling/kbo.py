# http://www.koreabaseball.com/TeamRank/TeamRank.aspx

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.koreabaseball.com/TeamRank/TeamRank.aspx')
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

table = soup.find('div', {'id': 'cphContainer_cphContents_udpRecord'}).find('table')
print(table)

ths = table.find_all('th')
for th in ths:
    print(th.text, end='\t')

print()
print('-' * 70)

trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(td.text, end='\t')
    print()

