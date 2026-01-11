arr=[1,2,3,4,5]

n=len(arr)
rev=[]
for i in range(n-1,-1,-1):
  rev.append(arr[i])

print("reversed=",rev)

