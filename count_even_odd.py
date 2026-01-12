arr = [10, 2, 3, 25, 18]

even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("even count =", even)
print("odd count =", odd)
