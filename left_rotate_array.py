arr = [1,2,3,4]

first = arr[0]

for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]

arr[-1] = first

print("Left rotated array =", arr)
