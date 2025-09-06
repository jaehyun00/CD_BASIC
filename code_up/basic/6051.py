cA, cB = input().split()

iA = int(cA)
iB = int(cB)

bResult = None

if iA != iB:
    bResult = True
elif iA == iB:
    bResult = False

print(bResult)