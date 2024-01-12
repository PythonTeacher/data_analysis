# 모듈 : 서로 연관된 작업들을 하는 코드들의 모임

# 모듈의 종류 : 표준 모듈, 사용자 생성 모듈, 서드 파티 모듈

import math

print(dir(math))
print(math.pi)

import mymath
print(dir(mymath))
print(mymath.pi)

# 모듈을 검색하는 경로
import sys
print(sys.path)

# 모듈 가져오는 방법
# 1. 일반 import : import 모듈명 -> 모듈명.함수명
# 2. 함수 import : from 모듈명 import 함수명 -> 함수명
# 3. 함수 전체 import : from 모듈명 import *

from mymath import *

print(pi)
print(add(10, 20))

# Alias 주기
from math import pi
from mymath import pi as my_pi

print(pi)
print(my_pi)

# 다양한 파이썬 모듈
import os

print(os.getcwd())

# 난수구하기
import random

for i in range(10):
    print(random.randint(1, 10), end=' ')
    print(random.randrange(1, 10), end=' ')


# HTTP 통신과 모듈
# URL에서 HTML 파일 가져오기
from urllib.request import urlopen

f = urlopen('http://www.python.org')

# 헤더 정보
print(f.headers)

# print(f.read())

# BeautifulSoup로 HTML Parsing
# pip install bs4

html = f.read()        # HTML 문서 읽기 (한번만 read하기)
print(html)

from bs4 import BeautifulSoup


# parser 종류
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

# 웹 브라우저 모듈
import webbrowser

# webbrowser.open('http://www.python.org')






























