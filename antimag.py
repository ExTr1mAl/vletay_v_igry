cubes = []
main_sum = 0
for k in range(1, 1001):
    if (k % 2 != 0):
        kyb = k**3 + 17
        cubes.append(kyb)
print(cubes)
for element_of_list in cubes:
    sum = 0
    for k in range(1, len(str(element_of_list)) + 1):
        sum += element_of_list % 10
        element_of_list = element_of_list // 10
    if (sum % 7 == 0):
        main_sum += element_of_list
    print(sum)


