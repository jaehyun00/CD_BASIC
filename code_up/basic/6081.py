cChar = input()
iHex = int(cChar, 16)

for i in range(1, 16):
    # print(cChar + '*' + str(i) + '=' + str(hex(iHex * i))[2:], sep='')
    print('%X' % iHex, '*%X' % i, '=%X' % (iHex * i), sep='')