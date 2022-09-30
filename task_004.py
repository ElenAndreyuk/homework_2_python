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
temp_list = data.readlines()
print(temp_list)

for line in data:
    temp =int( line)
    print(temp)
    result *= list_n[temp]
data.close()    
print(result)    

