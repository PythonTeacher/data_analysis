# 문자열 : "", ''

print("Hello", ', World!!')

print('I Love "IU"')

# 여러줄 문자열 출력
s = """
수지
아이유
하니
"""
print(s)

# 문자열 연결
a = "I" + " Love" + " IU"
print(a)

# 주의사항
# print(10 + "IU")

print('=' * 50)

# 문자열 길이 : len()
print(len(a))

# 문자열 포맷팅
# 1. 서식문자 사용 (%d, %f, %s)
print("ID : %d, NAME : %s" % (2301, "나파이"))

# 2. format() 사용
print("키 : ", format(185.34, ".1f"))
print("재산 : ", format(10000000000000, ",d"))

s = "I ate {} {}".format(5, "apples")
print(s)

s = "I ate {0} {1} and {0} {2}".format(5, "apples", "bananas")
print(s)

s = "I ate {num} {what}".format(num=5, what="kiwi")

# 문자열 함수
print(dir(s))

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

print(s.count('i'))

print(a)

# 문자열 결합
print(" ".join(a))

# 문자열 나누기
print(a.split())

# 문자열은 순서가 있다 -> indexing, slicing
print(a[0], a[2])

# 제일 마지막 문자를 출력해보자
print(a[len(a) - 1])
print(a[-1])

# slicing
# a = "I Love IU"
print("012345678901234567890")

# Love를 추출
print(a[2:6])
print(a[2:])
print(a[:])

# start:end-1:step
print(a[2::2])

# I Love IU를 거꾸로 찍으려면?
print(a[::-1])

# 학번을 slicing해서 기수, 학년, 반, 번호로 잘라내기
s = "142301"

gisu = s[:2]
grade = s[2:3]
ban = s[3:4]
number = int(s[-2:])

print("%s기 %s학년 %s반 %d번" % (gisu, grade, ban, number))

# 문자열 내용는 변경 불가
# s[3] = "4"








