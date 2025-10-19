cnt = int(input())
call = input().split()

list = [0 for i in range(23)]

for i in range(len(call)):
    call[i] = int(call[i])

for i in range(cnt):
    list[call[i] - 1] += 1

print(*list)