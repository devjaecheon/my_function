"""
2022년 11월 27일
코드 작성자 : 고재천
코드 이름 : utils.py
코드 목적 : 유용한 함수를 따로 저장 하여, 두고 나중에 불러와 사용 하기 위함.
"""


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)


def gugudan(x):
    for i in range(9):
        print((i + 1) * x)


def hanoi(n, f, t, via):
    if n == 1:
        print(str(f) + " -> " + str(t))
    else:
        hanoi(n - 1, f, via, t)
        print(str(f) + " -> " + str(t))
        hanoi(n - 1, via, t, f)