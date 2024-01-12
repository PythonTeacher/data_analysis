# 딕셔너리 : 키와 값으로 이루어진 자료형, 순서가 없음
# 순서가 없으므로 인덱싱, 슬라이싱을 하지 못한다.
# 리스트처럼 변경가능합니다.

a = {}
b = dict()
print(type(a), type(b))

d = {'apple': 1500, 'kiwi': 3000, 'banana': 2500}
print(d)

# 데이터 조회
print(d.get('apple', 0))
print(d['apple'])

# 데이터 추가
d['tomato'] = 500
print(d)

# 데이터 출력
for key in d.keys():
    print(key, d[key])

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

# 데이터 삭제
del d['tomato']
print(d)

# list comprehension : 1 ~ 10 사이의 홀수들의 제곱구하기
# [1, 9, 25, 49, 81]
l = [i ** 2 for i in range(1, 11) if i % 2]
print(l)

# 딕셔너리 comprehension
# {1:1, 3:9, 5:25, 7:49, 9:81}
d = {i: i ** 2 for i in range(1, 11) if i % 2}
print(d)

# 순서를 유지하는 딕셔너리
from collections import OrderedDict

od = OrderedDict()

od['one'] = 1
od['two'] = 2
od['three'] = 3

for key, value in od.items():
    print(key, value)

# 파일에서 데이터 읽어오기
f = open('nickname.txt', 'r', encoding='utf-8')

d = {}

# {'이상훈': '핫산', '김재하': '바야바', '송혜민': '둘리'}
for line in f:
    data = line.strip().split(':')
    d[data[0]] = data[1]

f.close()
print(d)

# 단어수를 세서 딕셔너리에 저장
# {'python': 3, 'and' : 4, '나바보': 3, ...}
f = open('python.txt', 'r', encoding='utf-8')

txt = f.read()
print(txt)

l = txt.lower().split()
print(l)

words = {}

for word in l:
    # if word in words:
    #     words[word] += 1
    # else:
    #     words[word] = 1
    words[word] = words.get(word, 0) + 1

f.close()
print(words)

# 빈도수가 가장 많은 TOP3 단어는?

# 카운터 객체 이용하기
from collections import Counter

c = Counter(words)
print(c)

print(c.most_common(3))




















