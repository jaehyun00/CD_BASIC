cRed, cGreen, cblue = input().split()

iRed = int(cRed)
iGreen = int(cGreen)
iBlue = int(cblue)

result = list()

for i in range(0, iRed):
    for j in range(0, iGreen):
        for k in range(0, iBlue):
            print(i, j, k)

print(iRed * iGreen * iBlue)

