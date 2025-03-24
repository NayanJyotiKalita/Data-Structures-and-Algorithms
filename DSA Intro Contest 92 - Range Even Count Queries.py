Range Even Count Queries

Problem Description
You are analyzing the number of even scores over a series of days. You have been given an array A of size N where each element represents a score for a specific day. 
Additionally, you have Q queries represented by a 2D array B of size Qx2. Each query consists of two integers B[i][0] and B[i][1].
For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]].

Problem Constraints
|A| = N
|B| = Q
1 <= N, Q <= 105
-109 <= A[i] <= 109
0 <= B[i][0] <= B[i][1] <= N - 1

Input Format
First argument A, is an 1-D array of size N.
Second argument B, is a 2-D array of size Qx2.

Output Format
Return an integer array.

Example Input
Input 1:
A = [1, 2, 3, 4]
B = [[0, 3],
     [2, 3]]
Input 2:
A = [2, 2]
B = [[0, 0],
     [1, 1]]

Example Output
Output 1:
[2, 1]
Output 2:
[1, 1]

Example Explanation
For Input 1:
Consider 0-based indexing:
Number of even elements from [0, 3] is 2.
Number of even elements from [2, 3] is 1.
For Input 2:
Number of even elements from [0, 0] is 1.
Number of even elements from [1, 1] is 1.


User Code

 class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def even_range_queries(self, A, B):
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i] = 1
            else:
                A[i] = 0
            
        for i in range(1, len(A)):
            A[i] = A[i-1] + A[i]
        
        c = []
        for i in range(len(B)):
            summ = 0
            l = B[i][0]
            r = B[i][1]
            if l == 0:
                summ = A[r]
            else:
                summ = A[r] - A[l-1]
            
            c.append(summ)
        
        return c


solution = Solution()
print(solution.even_range_queries( A = [1, 2, 3, 4], B = [[0, 3], [2, 3]] ))
