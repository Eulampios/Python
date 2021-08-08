for i in range(1, 101):
    if i == 1:
        print(i, 'процент')
    if i >= 5 and i <= 20:
        print(i, 'процентов')
    elif i >1 and i < 5:
        print(i, 'процента')
    if i > 20 and i % 10 == 1:
        print(i, 'процент')
    if i > 20 and i % 10 > 1 and i % 10 <= 4:
        print(i, 'процента')
    if i > 20 and i % 10 == 0:
        print(i, 'процентов')
    if i > 20 and i % 10 > 4 and i % 10 <= 9:
        print(i, 'процентов')
