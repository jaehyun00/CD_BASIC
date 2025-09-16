iStart = 1
canPrint = True

while (iStart > 0):
    cInput = input()

    if (canPrint):
        print(cInput)

    if (cInput == 'q'):
        canPrint = False
