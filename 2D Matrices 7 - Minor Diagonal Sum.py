Minor Diagonal Sum

Problem Description
You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).

Problem Constraints
1 <= N <= 103
-1000 <= A[i][j] <= 1000

Input Format
First and only argument is a 2D integer matrix A.

Output Format
Return an integer denoting the sum of minor diagonal elements.

Example Input
Input 1:
 A = [[1, -2, -3],
      [-4, 5, -6],
      [-7, -8, 9]]
Input 2:
 A = [[3, 2],
      [2, 3]]

Example Output
Output 1:
 -5 
Output 2:
 4 

Example Explanation
Explanation 1:
 A[1][3] + A[2][2] + A[3][1] = (-3) + 5 + (-7) = -5
Explanation 2:
 A[1][2] + A[2][1] = 2 + 2 = 4

CODE:

class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def minor_diagonal_sum(self, A):
        summ = 0
        n = len(A)
        for i in range(n):
            for j in range(n-1, -1, -1):
                if i+j == n-1:
                    summ += A[i][j]
        return summ

or

class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def minor_diagonal_sum(self, A):
        N = len(A)
        sum = 0
        for i in range(0, N):
            sum += A[i][N - 1 - i]
        return sum
     

solution = Solution()
print(solution.minor_diagonal_sum(A = [[1, -2, -3],
                                       [-4, 5, -6],
                                       [-7, -8, 9]]))
