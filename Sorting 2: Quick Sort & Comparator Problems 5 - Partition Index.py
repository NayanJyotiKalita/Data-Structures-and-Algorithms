Partition Index

Problem Description
Given an integer array A of length N, considering the last element as pivot p, rearrange the elements such that for all i:
if A[i] < p then it should be present on left side of the partition
if A[i] > p then it should be present on right side of the partition
Rearrange the given array as well as return the partition index.
Note: All elements are distinct

Problem Constraints
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 109

Input Format
The only input argument is the given vector A.

Output Format
Return the partition index as well as rearrange the input array to satisfy the given conditions.

Example Input
Input:
A = [6, 2, 0, 4, 5]
  
Example Output
Output:
 Valid
A possible solution can be:
A = [2, 0, 4, 5, 6] and partitionIndex = 3

CODE:

def partition(arr):
    p = arr[-1]  # Use the last element as the pivot
    i = 0  # This will track the partition index
    
    for j in range(len(arr) - 1):  # Loop through all elements except the pivot
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    # Place the pivot in its correct position
    arr[i], arr[-1] = arr[-1], arr[i]
    
    return i


solution = Solution()
print(solution.partition( A = [6, 2, 0, 4, 5] ))  -->  O/P:   Valid
                                                              A possible solution can be:
                                                              A = [2, 0, 4, 5, 6] and partitionIndex = 3
