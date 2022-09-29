# Задайте список из n чисел последовательности 
# по формуле (1+ 1 /n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2, 2, 2, 2, 2, 3]   13
n = int(input('введите число: '))
list_n =[]
for i in range(1, n+1):
    temp = round( (1 + 1/i)**i )
    list_n.append(temp)

print(list_n)
sum = 0
for j in list_n:
    sum +=j
print(sum)    
