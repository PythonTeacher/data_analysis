s = "abcdef가나다"

# a b c d e f 가 나 다

for x in s:
    print(x, end=' ')

print(" ".join(s))

# 숫자를 반복해서 쓸 경우 range() 함수 사용
for x in range(10):   # 0 ~ 9
    print(x, end=' ')

# 1부터 10까지의 합
tot = 0
for x in range(1, 11):
    tot += x

print(tot)

# sum 내장함수 사용
print(sum(range(1, 11)))

# 2 ~ 9단까지 구구단 출력
for i in range(2, 10):          # 2 ~ 9
    for j in range(1, 10):      # 1 ~ 9
        print("%d * %d = %2d\t" % (i, j, i * j), end='')
    print()
else:
    print('구구단 출력 끝!!')
