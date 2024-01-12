# bool 타입 : True, False

a = 1

print(a < 0, a > 0, a == 0, a != 0)
print("abcd" > "abb")

# bool()
print(bool(a))
print(bool(0))
print(bool("hello"))
print(bool(""))

# 논리 연산 (and, or, not)
print(True and True)
print(True and False)

print(True or False)
print(False or False)

print(not True)

a = 10
b = 0

# print(a / b)

# Short-circuit 테스트
if True or (a / b):
    print("Yes")
else:
    print("No")




