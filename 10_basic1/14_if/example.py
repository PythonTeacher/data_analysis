a = 10

# a가 0보다 크고 20보다 작냐?
# if a > 0 & a < 20:
if 0 < a < 20:
    print('True')
else:
    print('False')

# 입력받은 함수 : input()
num = int(input("금액 입력 =>"))

# 0이상이면 양수, 0보다 작으면 음수
if num > 0:
    print("양수")
elif num == 0:
    print("0입니다")
else:
    print("음수")


"""
현금이 2500원 이상이거나 카드가 있으면 추억의 라보떼를 사먹고,
현금만 1000원 이상있으면 누가바를 사먹고,
그 이외는 외상!!
"""
cash = 2000
isCard = False

if cash >= 2500 | isCard:
    print("라보떼")
elif cash >= 1000:
    print("누가바")
else:
    print("외상")








