# https://developers.skplanetx.com/
# 0d2d7502-5251-3b3b-89ae-3fb5153d0f3d
from urllib.request import urlopen, Request
import json

apiKey = "4ce8bb31-9934-376b-8a64-0b5922ad9f71"
page = "1"
count = "10"

url = "http://apis.skplanetx.com/melon/charts/realtime?"\
        "version={version}&page={page}&count={count}"\
        .format(version=1, page=page, count=count)

req = Request(url)
req.add_header('appKey', apiKey)

f = urlopen(req)

print(f.headers)

body = f.read()
print(body)

s = body.decode("utf-8")

j = json.loads(s)
# print(type(j), j)

from pprint import pprint
pprint(j)

# 1. 노래제목1 - 가수명1, 가수명2, 가수명3
# 2. 노래제목2 - 가수명4

# 검색결과 파싱하기
songs = j['melon']['songs']['song']

for song in songs:
    print('%s. %s - ' % (song['currentRank'], song['songName']), end='')
    artists = song['artists']['artist']
    for artist in artists:
        print('%s ' % artist['artistName'], end='')
    print()






