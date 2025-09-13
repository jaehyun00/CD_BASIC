cInput1 = input()

iInput1 = int(cInput1)

if iInput1 >= 90 and iInput1 <= 100:
    grade = 'A'
elif iInput1 >= 70 and iInput1 <= 89:
    grade = 'B'
elif iInput1 >= 40 and iInput1 <= 69:
    grade = 'C'
elif iInput1 >= 0 and iInput1 <= 39:
    grade = 'D'

print(grade)