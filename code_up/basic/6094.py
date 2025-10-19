cnt = int(input())
call = input().split()

for i in range(len(call)):
    call[i] = int(call[i])

min = call[0]

for i in call:
    if i < min:
        min = i

print(min)