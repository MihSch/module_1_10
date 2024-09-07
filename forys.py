# for i in 1, 2, 3, 4:    #переменная i будет существовать только в пределах цикла
#     print(i)
# list_ = ['one', 'two', 'three'] # итерабильные - значения которые можно перебрать
# list_2 = [2, 3, 4, 5, 1]
# for i in list_: #for это переборщик
#     if i == 'three':
#         list_.remove(i)
#
# print(list_)
# sum_ = 0
# for i in range(len(list_2)):  # range - возвращает послед чисел от 0 до числа в скобках
#     sum_ += list_2[i]
#
# print(sum_)
from module_1_7 import dict1

# for i in range(1, 11): #i-1 range вкл в себя start, stop, step
#     for j in range(1, 11): # j-1,2,3... последняя цифра послед не включается в список
#         print(f'{i} x {j} = {i*j}') # вывели ТАБЛ УМНОЖЕНИЯ
#
# dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
#
# for i, k in dict1.items():
#     print(i, k) # i будет ключом


                # Домашняя РАБОТА

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num == 1:
        continue
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
print("Primes:", primes)
print("Not Primes:", not_primes)

