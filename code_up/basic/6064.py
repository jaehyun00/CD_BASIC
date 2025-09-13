cInput1, cInput2, cInput3 = input().split()

iInput1 = int(cInput1)
iInput2 = int(cInput2)
iInput3 = int(cInput3)

print((iInput1 if (iInput1 < iInput2) else iInput2) if ((iInput1 if (iInput1 < iInput2) else iInput2) < iInput3) else iInput3)
