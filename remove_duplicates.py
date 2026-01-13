arr=[1,2,2,3,45,]
unique=[]
for i in arr:
  if i not in unique:
    unique.append(i)

print("array after removing duplicates=",unique)
