# 파일 읽고 쓰기

# 파일 쓰기
s = '여자친구가 짱이지!!\n하늘이가 좋아하지요'

f = open('python.txt','w', encoding='utf-8')
f.write(s)
f.close()

# 파일 읽기
f = open('python.txt', 'r', encoding='utf-8')
s = f.read()
print(s)
f.close()

# with문으로 파일 입출력하기
with open('python.txt', encoding='utf-8') as f:
    print(f.read())

l = ['짜장면', '짬뽕', '치킨', '라면']

s = '\n'.join(l)
print(s)

with open('python1.txt', 'w', encoding='utf-8') as f:
    f.write(s)

with open('python1.txt', 'r', encoding='utf-8') as f:
    print(f.read())


# 라인단위 읽기
# 1) 파일 객체의 반복자를 이용하기
with open('python1.txt', encoding='utf-8') as f:
    for line in f:
        print(line)

# 2) readline()
with open('python1.txt', encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()


# JSON 파일
import json

data = ''
with open('data.json', encoding='utf-8') as f:
    data = f.read()

print(data, type(data))

# str -> dict 변환
d = json.loads(data)
print(d, type(d))

# 아이유, 너랑나 출력
print(d.get("name"))
print(d["song"][1])

# dict -> str으로 변환
s = json.dumps(d, ensure_ascii=False)
print(s, type(s))

















