Highest Product (Greedy Algorithm)

Problem Description
Given an integer array A of size N.
Return the highest product possible by multiplying 3 numbers from the array.
NOTE: Solution will fit in a 32-bit signed integer.

Problem Constraints
1 <= N <= 5* 105

Input Format
The first and the only argument is an integer array A.

Output Format
Return an integer denoting the highest possible product.

Example Input
A = [0, -1, 3, 100, 70, 50]
Example Output
350000

Example Explanation
70 * 50 * 100 = 350000

CODE

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort()
        n = len(A)
        p1 = A[n-1] * A[n-2] * A[n-3]
        p2 = A[0] * A[1] * A[n-1]
        return max(p1, p2) 


solution = Solution()
print(solution.maxp3( A = [0, -1, 3, 100, 70, 50] ))  -->  O/P: 350000
