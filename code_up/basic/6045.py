cInput1, cInput2, cInput3 = input().split()

iInput1 = int(cInput1)
iInput2 = int(cInput2)
iInput3 = int(cInput3)

iSum = iInput1 + iInput2 + iInput3
iAvg = (iInput1 + iInput2 + iInput3) / 3

print(iSum, format(iAvg, '.2f'))
