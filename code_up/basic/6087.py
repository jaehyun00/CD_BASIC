cnt = input()
cnt = int(cnt)

for i in range(1, cnt + 1):
    if i % 3 == 0:
        continue
    else:
        print(i, end=' ')