cInput = input()
iInput = int(cInput)
arrValidate = ('3', '6', '9')
result = list()

for i in range(1, iInput + 1):
    containCnt = 0
    for j in str(i):
        if (j in arrValidate):
            containCnt += 1
    if (containCnt > 0):
        result.append('X' * containCnt)
    else:
        result.append(i)

print(*result)