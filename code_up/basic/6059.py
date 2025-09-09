# n = bin(int(input))
# ~n = -n - 1
# -n = ~n + 1 => -n - 1 + 1 => -n

iInput = int(input())

bInput = bin(iInput)
bInput_reverse = bin(~iInput)

iInput_reverse = int(bInput_reverse, 2)

print(iInput_reverse)

