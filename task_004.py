# Задайте список из N элементов, заполненных 
# числами из промежутка [-N, N]. Найдите 
# произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('введите число: '))
list_n = []
for i in range(-n, n+1):
    list_n.append(i)

print(list_n)

result = 1

data = open('file.txt', 'r')
# temp = data.read().split("\n")
# print(temp)
for line in data:
    temp = [data.read().split("\n")]
    print(temp)
    for j in temp:
        result *= int(j)
data.close()    
print(result)    

