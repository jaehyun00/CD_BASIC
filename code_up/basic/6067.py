cInput1 = input()

iInput1 = int(cInput1)

if iInput1 < 0 and iInput1 % 2 == 0:
    print('A')
elif iInput1 < 0 and iInput1 % 2 == 1:
    print('B')
elif iInput1 > 0 and iInput1 % 2 == 0:
    print('C')
elif iInput1 > 0 and iInput1 % 2 == 1:
    print('D')