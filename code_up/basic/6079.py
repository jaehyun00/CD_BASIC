iInput = int(input())
iStart = 1
iAcc = 0

while True:
    iAcc += iStart

    if (iAcc >= iInput):
        break

    iStart += 1

print(iStart)



