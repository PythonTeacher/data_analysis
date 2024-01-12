# 숫자 자료형 : 정수형, 실수형, 복소수형

# 정수형 (int)
a = 10
print(a, type(a))

# 실수형 (float)
b = 3.14
print(b, type(b))

# 숫자 연산
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)   # 몫을 리턴
print(a ** b)   # 거듭제곱
c, d = divmod(a, b)     # 몫, 나머지 같이 리턴
print(c, d)

# 형변환
x = 36
y = -10.4
z = 1.23456789

print(float(x))
print(int(y))

print("=" * 50)

# dir : 객체가 가지고 있는 변수나 함수의 목록을 보여줌
print(dir(x))

import math
print(dir(math))
print(math.pi)









