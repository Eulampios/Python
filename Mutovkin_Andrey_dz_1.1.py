input_sec = int(input('Введите секунды: '))
minutes = input_sec // 60
seconds = input_sec % 60
hours = input_sec // 3600
if input_sec < 60:
    print(input_sec, 'сек.')
elif input_sec >= 60 and input_sec < 3600:
    print(minutes, 'мин.', seconds, 'сек.')
elif input_sec >= 3600:
    print(hours, 'ч.', int((input_sec / 3600 - input_sec // 3600) * 60), 'мин.', seconds, 'сек.')

print(input('\n\nнажмите Enter, чтобы выйти'))
