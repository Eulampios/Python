# Список из кубов чисел от 1 до 1000
list = []
for i in range(1, 1001, 2):
    list.append(i ** 3)
print(list)

# Пункт а)

sum_num = 0 # итоговый ответ
for i in list:
    sum_dig = 0
    for j in str(i):
        sum_dig += int(j)
    if sum_dig % 7 == 0:
        sum_num += i
print(sum_num)

# Пункт b, c)

sum_num = 0
for i in list:
    i += 17
    sum_dig = 0
    for j in str(i):
        sum_dig += int(j)
    if sum_dig % 7 == 0:
        sum_num += i
print(sum_num)