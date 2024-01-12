import time

# 함수 기본형
def add(a, b):
    return a + b

print(add(3, 4))
print(add(1.2, 3.4))
print(add("Hi", " Guys"))


def plus_minus(a, b):
    return a + b, a - b

x, y = plus_minus(3, 5)

print(x, y)


# 매개변수의 디폴트 값 설정
def add(a=1, b=2):
    return a + b

print(add())
print(add(5))
print(add(5, 10))

# 키워드로 매핑하기
print(add(a=7))
print(add(b=9))


# 가변인자 함수
def sum_many(*args):
    print(args)
    return sum(args)

print(sum_many())
print(sum_many(10))
print(sum_many(10, 20))
print(sum_many(10, 20, 30))


# 키워드 가변인자 함수
# d = {'kor':100, 'mat':90, 'eng':80}

def print_score(**kwargs):
    print(kwargs)
    tot = 0
    for subject in kwargs:
        print("과목명 : %s, 점수 : %d" % (subject, kwargs[subject]))
        tot += kwargs[subject]
    print("총점 : %d점, 평균 : %.1f점" % (tot, tot / len(kwargs)))


print_score(kor=100, mat=95, eng=90)


# 재귀함수
# 카운트다운 로켓 발사
def countdown(n):
    if n == 0:
        print("로켓 발사!!")
    else:
        print("count =>", n)
        time.sleep(1)
        countdown(n - 1)

# countdown(10)

# 람다 함수 : 이름이 없는 함수
# 형식) lambda 입력값: 표현식 -> 표현식 결과가 리턴됨

func = lambda x, y: x * y
print(func(3, 4))

print((lambda x, y: x * y) (3, 4))

print((lambda : 'no input') ())




















