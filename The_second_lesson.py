# 1-ая задача
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 2-ая задача
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
stri = ''
for k in list:
    if (k.isdigit() == True):
        if (len(k) == 1):
            k = '"' + '0' + k + '"'
    if (k.isdigit() == True):
        if (len(k) == 2):
            k = '"' + k + '"'
    if ('+' in k):
        k = k.strip('+')
        k = f' "+0{k}" '
    stri = stri + k + ' '
print(stri)

# 4-ая задача
names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
string = ''
for k in names:
    idx = k.rfind(' ')
    name = 'Привет ' + k[idx+1:].lower().capitalize() + '!'
    string += name + ' '
print(string)

# 5-ая задача
cost_things = [10.6, 12, 90, 7, 12, 6.54, 21, 90, 32, 1]
cost_things = sorted(cost_things, reverse=False)
other_cost_things = [10.6, 12, 90, 7, 12, 6.54, 21, 90, 32, 1]
other_cost_things = sorted(other_cost_things, reverse=True)
b = ''
a = ''
i = 0
for k in cost_things:
    n = str(k)
    if (type(k) == float):
        index = n.find('.')
        if (len(n[index+1:]) == 2):
            n = n[0:index] + ' руб ' + n[index+1:] + ' коп'
        else:
            n = n[0:index] + ' руб ' + n[index + 1:] + '0' + ' коп'
    else:
        n = n + ' руб' + ' 00' + ' коп'
    i += + 1
    if(len(cost_things) == i):
        a += n + '.'
    else:
        a += n + ', '
print(a)

m = 0
for k in other_cost_things:
    n = str(k)
    if (type(k) == float):
        index = n.find('.')
        if (len(n[index+1:]) == 2):
            n = n[0:index] + ' руб ' + n[index+1:] + ' коп'
        else:
            n = n[0:index] + ' руб ' + n[index + 1:] + '0' + ' коп'
    else:
        n = n + ' руб' + ' 00' + ' коп'
    m += + 1
    if (len(other_cost_things) == m):
        b += n + '.'
    else:
        b += n + ', '
print(b)

j = 0
c = ''
for k in cost_things[5:]:
    n = str(k)
    if (type(k) == float):
        index = n.find('.')
        if (len(n[index+1:]) == 2):
            n = n[0:index] + ' руб ' + n[index+1:] + ' коп'
        else:
            n = n[0:index] + ' руб ' + n[index + 1:] + '0' + ' коп'
    else:
        n = n + ' руб' + ' 00' + ' коп'
    j += + 1
    if(len(cost_things[5:]) == j):
        c += n + '.'
    else:
        c += n + ', '
print(c)