cnt = int(input())
call = input().split()

for i in range(len(call)):
    call[i] = int(call[i])

# print(*reversed(call))
for i in range(len(call) - 1, -1, -1):
    print(call[i], end=' ')