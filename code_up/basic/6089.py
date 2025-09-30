# a = 시작값, r = 등비값, n = 몇번째 수
a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

print(a * pow(r, n-1))

