#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.

def max_sum_of_2(a: int, b: int, c: int) -> int:
    sum1=a+b
    sum2=a+c
    sum3=b+c
    if sum1>sum2 and sum1>sum3 and sum1!=sum2 and sum1!=sum3:
        sum=sum1
    elif sum2>sum1 and sum2>sum3 and sum2!=sum1 and sum2!=sum3:
        sum=sum2
    elif sum3>sum1 and sum3>sum2 and sum3!=sum1 and sum2!=sum3:
        sum=sum3
    elif sum1==sum2 and sum1!= sum3 and sum1>sum3:
        sum=sum1
    elif sum1==sum2 and sum1!=sum3 and sum1<sum3:
        sum=sum3
    elif sum2 == sum3 and sum2!=sum1 and sum1 < sum3:
        sum = sum3
    elif sum3==sum2 and sum2!=sum1 and sum1>sum3:
        sum=sum1
    elif sum1==sum3 and sum1!=sum2 and sum1<sum2:
        sum=sum2
    elif sum1==sum3 and sum1!=sum2 and sum1>sum2:
        sum=sum1
    else:    #sum1=sum2=sum3
        sum=sum1



    return sum

if __name__ == "__main__":

    a = int(input("Наминал первой монетки a = "))
    b = int(input("Наминал второй монетки b = "))
    c = int(input("Наминал третьей монетки c = "))

    print('Максимальная сумма двух монеток: ', max_sum_of_2(a, b, c))
