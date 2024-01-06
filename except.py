try:
    z = [i for i in input().split(" ")]
    z = list(map(int, z))
    f = int(input())
    res = sum(z) / f
except ValueError:
    print("Допустимо вводить только числа через пробел")
except ZeroDivisionError:
    print('В качестве знаменателя не может быть ноль')
except:
    print('Неизвестная ошибка')
print('Штатное завершение программы')
