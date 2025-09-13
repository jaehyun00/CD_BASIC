cInput1 = input()

iStart = ord('a')
iEnd = ord(cInput1)

while iEnd - iStart >= 0:
    print(chr(iStart) + ' ', end='')
    iStart += 1