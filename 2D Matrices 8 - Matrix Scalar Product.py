Matrix Scalar Product

Problem Description
You are given a matrix A and and an integer B, you have to perform scalar multiplication of matrix A with an integer B.
  
Problem Constraints
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000
1 <= B <= 1000

Input Format
First argument is 2D array of integers A representing matrix.
Second argument is an integer B.

Output Format
You have to return a 2D array of integers after doing required operations.

Example Input
Input 1:
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2 
Input 2:
A = [[1]]
B = 5 

Example Output
Output 1:
[[2, 4, 6], 
[8, 10, 12], 
[14, 16, 18]]
Output 2:
[[5]]

Example Explanation
Explanation 1:
==> ( [[1, 2, 3],[4, 5, 6],[7, 8, 9]] ) * 2
==> [[2*1, 2*2, 2*3],
     [2*4, 2*5, 2*6],
     [2*7, 2*8, 2*9]]
==> [[2,   4,  6], 
     [8,  10, 12], 
     [14, 16, 18]]

Explanation 2:
==> ( [[1]] ) * 5
==> [[5*1]]
==> [[5]]

CODE:

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def scalar_product(self, A, B):
        c = []
        for i in range(len(A)):
            inner_list = []
            for j in range(len(A[0])):
                inner_list.append(B*A[i][j])
            c.append(inner_list)
        return c

solution = Solution()
print(solution.scalar_product(A = [[1, 2, 3],
                                   [4, 5, 6],
                                   [7, 8, 9]], B = 2))
