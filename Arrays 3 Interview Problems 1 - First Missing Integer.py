First Missing Integer

Problem Description
Given an unsorted integer array, A of size N. Find the first missing positive integer.
Note: Your algorithm should run in O(n) time and use constant space.

Problem Constraints
1 <= N <= 1000000
-109 <= A[i] <= 109

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the first missing positive integer.

Example Input
Input 1:
[1, 2, 0]
Input 2:
[3, 4, -1, 1]
Input 3:
[-8, -7, -6]

Example Output
Output 1:
3
Output 2:
2
Output 3:
1

Example Explanation
Explanation 1:
A = [1, 2, 0]
First positive integer missing from the array is 3.
Explanation 2:
A = [3, 4, -1, 1]
First positive integer missing from the array is 2.
Explanation 3:
A = [-8, -7, -6]
First positive integer missing from the array is 1.

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):

        n = len(A)

        for i in range(n):
            if A[i] <= 0:
                A[i] = n + 2
        
        for i in range(n):
            ele = abs(A[i])
            if ele >= 1 and ele <= n:
                idx = ele - 1
                A[idx] = -1 * abs(A[idx])
        
        for i in range(n):
            if A[i] > 0:
                return i + 1
        
        return n + 1

'or'

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        a = [0] * (n + 1)

        for i in range(n):
            if A[i] >= 1 and A[i] <= n:
                a[A[i] - 1] = 1
        
        for i in range(len(a)):
            if a[i] == 0:
                return i + 1


solution = Solution()
print(solution.firstMissingPositive( A = [3, 4, -1, 1] ))
