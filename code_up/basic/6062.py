cInput1, cInput2 = input().split()

iInput1 = int(cInput1)
iInput2 = int(cInput2)

# cBin1 = bin(iInput1)
# cBin2 = bin(iInput2)

cBinChars = bin(iInput1 ^ iInput2)
iBinChars = int(cBinChars, 2)

print(iBinChars)