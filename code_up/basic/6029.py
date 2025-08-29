#'%o' = 8진수
cInput = input()

#int(String, Base)
hInput = int(cInput, 16)

iOctal = '%o' % hInput

print(iOctal)