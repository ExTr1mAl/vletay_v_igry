duration = input('Введите, пожалуйста, время в секундах: ')
duration = int(duration)
min = 60
hour = 3600
day = hour*24

if (duration < min):
    print(duration, 'сек')
elif (duration < hour):
    print(duration // min, 'мин', duration % min, 'сек')
elif (duration < day):
    print(duration // hour, 'час', duration % hour // min, 'мин', duration % hour % min, 'сек')
elif (duration > day):
    print(duration // day, 'день(ей)', duration % day // hour, 'час', duration % day % hour // min, 'мин', duration % day % hour % min, 'сек')
