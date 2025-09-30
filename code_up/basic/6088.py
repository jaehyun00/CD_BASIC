# a = 시작값, d = 등차값, n = 몇번째 수
a, d, n = input().split()

a = int(a)
d = int(d)
n = int(n)

print(a + (d * (n - 1)))

