arr = [10, 25, 3, 46, 18]
key = 46

found = False

for i in arr:
    if i == key:
        found = True
        break 

if found:
    print("element found")
else:
    print("element not found")
