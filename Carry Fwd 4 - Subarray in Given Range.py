Subarray in given range

Problem Description
Given an array A of length N, return the subarray from B to C.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
0 <= B <= C < N

Input Format
The first argument A is an array of integers
The remaining argument B and C are integers.

Output Format
Return a subarray

Example Input
Input 1:
A = [4, 3, 2, 6]
B = 1
C = 3
Input 2:
A = [4, 2, 2]
B = 0
C = 1

Example Output
Output 1:
[3, 2, 6]
Output 2:
[4, 2]

Example Explanation
Explanation 1:
The subarray of A from 1 to 3 is [3, 2, 6].
Explanation 2:
The subarray of A from 0 to 1 is [4, 2].

CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def subarray_in_range(self, A, B, C):
        d = []
        for i in range(B, C+1):
            d.append(A[i])
        return d

'or'

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def subarray_in_range(self, A, B, C):
        return A[B : C + 1]


solution = Solution()
print(solution.subarray_in_range(A = [4, 3, 2, 6], B = 1, C = 3))  -->  O/P: [3, 2, 6]
