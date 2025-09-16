iInput1 = int(input())
iResult = 0

for i in range(1, iInput1 + 1):
    if (i % 2 == 0):
        iResult += i

print(iResult)