# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input('Введите число N: '))

def mnoj(n):
    result = list()
    d = 2
    while d <= n:
        if n % d == 0:
            result.append(d)
            n = n/d
        else:
            d += 1
    return(result)

print(mnoj(N))                
