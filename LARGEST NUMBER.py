### Description

This Python program finds the largest element in a given array.
It initializes the first element as the maximum value and then compares it with all other elements in the array.
If a larger element is found, it updates the maximum value.
Finally, the program prints the largest element in the array.

### Time Complexity

The time complexity of this program is O(n), where n is the number of elements in the array.
arr=[10,25,3,46,18]

max_element=arr[0]
for i in arr:
    if i > max_element:
        max_element=i
        
print("largest element",max_element)
