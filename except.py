try:
    z = [i for i in input().split(" ")]
    z = list(map(int, z))
    f = int(input())
    try:
        res = sum(z) / f
    except ZeroDivisionError as z:
        print(z)
except ValueError:
    print("Допустимо вводить только числа через пробел")
else:
    print("Штатное выполнение программы")
finally:
    print("Анализ закончен")
