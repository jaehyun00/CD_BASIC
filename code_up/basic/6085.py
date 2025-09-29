w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)

# print(round(((((w * h * b) / 8) / 1024)) / 1024, 2), 'MB')
print('{:.2f} MB'.format(((((w * h * b) / 8) / 1024)) / 1024))

 