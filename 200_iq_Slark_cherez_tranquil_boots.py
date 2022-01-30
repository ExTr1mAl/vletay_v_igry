percent = 'процент'
for k in range(1, 101):
    n = str(k)
    if (n[len(n)-1] == '1') and (k != 11):
        print(k, percent)
    elif k in range(11, 21):
        print(k, percent + 'ов')
    elif (n[len(n)-1] == '2') or (n[len(n)-1] == '3') or (n[len(n)-1] == '4'):
        print(k, percent + 'a')
    else:
        print(k, percent + 'ов')

