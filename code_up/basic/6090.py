# a = 시작값, m = 곱할 값, d = 더할값, n = 몇번째 수
a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

s = a

for i in range(n - 1):
    s = s * m + d

print(s)
