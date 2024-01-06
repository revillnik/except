def check_zero(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError as z:
        print(z)
try:
    z = [i for i in input().split(" ")]
    z = list(map(int, z))
    f = int(input())
    check_zero(sum(z), f)
except ValueError:
    print("Допустимо вводить только числа через пробел")
else:
    print("Штатное выполнение программы")
finally:
    print("Анализ закончен")
