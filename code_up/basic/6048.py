cInput1, cInput2 = input().split()

iInput1 = int(cInput1)
iInput2 = int(cInput2)

bResult = None

if iInput1 < iInput2:
    bResult = True
elif iInput1 >= iInput2:
    bResult = False

print(bResult)