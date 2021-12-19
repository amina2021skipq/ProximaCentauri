#Remove Duplicates from Sorted Array
#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

def removeDuplicates(arr, n):
    if n == 0 or n == 1:
        return n
 
    temp = list(range(n))
 
    # Start traversing elements
    j = 0;
    for i in range(0, n-1):
 
        # If current element is
        # not equal to next
        # element then store that
        # current element
        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1
 
    # Store the last element
    # as whether it is unique
    # or repeated, it hasn't
    # stored previously
    temp[j] = arr[n-1]
    j += 1
     
    # Modify original array
    for i in range(0, j):
        arr[i] = temp[i]
 
    return j
 
# Driver code
arr = [1, 2, 2, 5, 6, 2, 8, 2, 1, 1]
n = len(arr)
 
# removeDuplicates() returns
# new size of array.
n = removeDuplicates(arr, n)
 
# Print updated array
for i in range(n):
    print(arr[i])
  