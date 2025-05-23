Sort 01

Problem Description
Given an array A of 0s and 1s of length N. Sort this array.
Note - Do not use any sorting algorithm or library's sort method.

Problem Constraints
1 ≤ N ≤ 105
0 ≤ A[i] ≤ 1

Input Format
First argument A is an array of length N.

Output Format
Return the sorted array.

Example Input
Input 1:
A = [0,0,1,0,1,1,0]
Input 2:
A = [1,0]

Example Output
Output 1:
[0,0,0,0,1,1,1]
Output 2:
[0,1]

CODE:

import functools
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sort01(self, A):
        A = sorted(A, key = functools.cmp_to_key(self. compare))
        return A
    
    def compare(self, v1, v2):
        return v1 - v2

'or'

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sort01(self, A):
        n = len(A)
        i, j = 0, n - 1
        while i < j:
            if A[i] == 1:
                A[i], A[j] = A[j], A[i]
                j -= 1
            else:
                i += 1
        return A

'or'

import functools
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sort01(self, A):
        zeros=A.count(0)
        ones=len(A)-zeros
        A=[0]*len(A)
        if zeros==len(A):
            return A 
        else:
            for i in range(zeros,len(A)):
                A[i]=1
        return A


solution = Solution()
print(solution.sort01( A = [0,0,1,0,1,1,0] )  -->  O/P: [0,0,0,0,1,1,1]
