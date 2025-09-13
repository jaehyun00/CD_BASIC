cInput1 = input()

iInput1 = int(cInput1)

if iInput1 // 3 == 1:
    print('spring')
elif iInput1 // 3 == 2:
    print('summer')
elif iInput1 // 3 == 3:
    print('fall')
elif iInput1 // 3 == 0 or iInput1 // 3 == 4:
    print('winter')