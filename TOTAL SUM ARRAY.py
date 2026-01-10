### Description

## This Python program calculates the sum of elements in an array (list) entered by the user.
## The user first provides the number of elements, then enters each value.
## The program stores the values in a list and uses a loop to compute and display the total sum.

### Time Complexity

## The time complexity of this program is **O(n)**, where `n` is the number of elements in the array.


n=int(input("enter number"))
arr=[]
for i in range(n):
    arr.append(int(input()))
total=0
for i in range(n):
   total +=arr[i]

print("sum=",total)
