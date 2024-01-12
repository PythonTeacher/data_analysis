# 리스트 : 순서(시퀀스)를 가지는 객체들의 집합, 변경이 가능함
# 인덱싱, 슬라이싱 가능

a = []
b = list()
print(a, type(a), b, type(b))

a = [1, 2, "python"]

# 인덱싱
print(a[0], a[-1])

# for문으로 값 순차 출력
for i in a:
    print(i)

for i, data in enumerate(a):
    print("%d, %s" % (i, data))

# 슬라이싱 (start:end-1:interval)
# 2, 3번째 데이터 출력 (2, python)
print(a[1:3], a[1:], a[-2:])
print(a[::2])

# 리스트 뒤집기 (python, 2, 1)
print(a[::-1])

print(a * 2)

print(a + [3, 4, 5])

print(a)

l = ["c", "c++", "java", "python"]

# c를 포함하고 있는 모든 문자열을 출력해보자 (c, c++)
for i in l:
    if 'c' in i:
        print(i)

# 값 변경
l[2] = "php"
print(l)

l[0:2] = ["html", "css"]
print(l)

# 리스트에 있는 값을 하나의 문자열 연결
print(' '.join(l))

# python 내장함수
l = [1, 2, 3]

print(len(l))
print(sum(l))

l.append(4)
print(l)

l.insert(3, 1)
print(l)

print(l.count(1))

l.sort()
print(l)

l.reverse()
print(l)

l.remove(1)
print(l)

# 중첩리스트
l = [1, 2, 3]
t = ['start', l, 'end']
print(t)

# 2 출력하기
print(t[1][1])

# 삼중리스트
l = [1, ["a", ["x", "y"], "b"], 2]

# y 출력하기
print(l[1][1][1])

# range : 숫자 리스트를 자동으로 생성해주는 함수(start, end-1)
for i in range(1, 11):     # 1 ~ 10
    print(i, end=' ')

# 1~10사이의 숫자를 제곱한 결과를 갖는 리스트를 만들자
l = []
for i in range(1, 11):
    l.append(i ** 2)

print(l)

# map 함수
# 형식) map(함수, <iterable>)
# 리스트에 들어있는 값들을 함수에 하나씩 적용한다.
def square(x):
    return x ** 2

print(list(map(square, [1, 2, 3, 4, 5])))

# 람다함수 + map 함수
print(list(map(lambda x: x ** 2, range(1, 6))))

# 문자열 : apple -> [aa, pa, pa, la, ea]
print(list(map(lambda x: x + "a", "apple")))

# List Comprehension (C 모듈로 되어 있어 속도가 짱!!!)
# 형식) [출력식 for문 <iterable> (if 조건문)]
print([x ** 2 for x in range(1, 6)])

# filter 함수
# 형식) filter(함수, <iterable>)
# 리스트에 들어있는 값을 함수에 적용하여 결과가 참인 경우만 골라낸다.
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# 람다함수 + filter 함수
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

# 1 ~ 10까지 숫자 중 홀수만 리턴하기
print(list(filter(lambda x: x % 2, range(1, 11))))

# 1 ~ 10까지 숫자 중 홀수만 제곱하기 [1, 9, 25, 49, 81]
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 11)))))

# List Comprehension으로 만들어보기
l = [x ** 2 for x in range(1, 11) if x % 2]
print(l)

# 각 단어의 길이를 출력해보자
s = "May the force be with you"   # [3, 3, 5, 2, 4, 3]
words = s.split()
print(words)

print(list(map(lambda word: len(word), words)))
print([len(word) for word in words])

# 위에 문장에서 자음만 뽑아서 출력해보자 (aeiou를 제외)
print(list(filter(lambda x: x not in "aeiou", s)))
print([x for x in s if x not in "aeiou"])

# hw) 10보다 작은 3 또는 5의 배수는 3, 5, 6, 9 -> 23
# 1000보다 작은 3 또는 5의 배수의 합을 구하기
# 234168
import time

s = time.time()
print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(10000000))))
e = time.time()
print("lambda => ", str(e - s))

s = time.time()
print(sum([x for x in range(10000000) if x % 3 == 0 or x % 5 == 0]))
e = time.time()
print("list comprehension => ", str(e - s))









