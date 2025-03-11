Positive in Range

Problem Description
You are working on a project to analyze profit for a given set of days. You have been given an array A with profit for N days. You also have Q queries represented by a 2D array B of size Qx2. Each query consists of two integers B[i][0] and B[i][1].
For every query, your task is to find the count of non-negative profit in the range from A[B[i][0]] to A[B[i][1]].

Problem Constraints
|A| = N
|B| = Q
1 <= N, Q <= 105
-109 <= A[i] <= 109
0 <= B[i][0] <= B[i][1] <= N - 1

Input Format
First arguemnt A, is an array
Second argument B, is a matrix

Output Format
Return an array.

Example Input
Input 1:
A = [1, -1, 0]
B = [[0, 2],
    [1, 2]]
Input 2:
A = [-1, -2]
B = [[0, 0],
    [1, 1]]

Example Output
Output 1:
[2, 1]
Output 2:
[0, 0]

Example Explanation
For Input 1:
Consider 0-based indexing:
Number of non-negative elements from [0, 2] is 2.
Number of non-negative elements from [1, 2] is 1.
For Input 2:
Number of non-negative elements from [0, 0] is 0.
Number of non-negative elements from [1, 1] is 0.

CODE:

 class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def positive_in_range(self, A, B):
        n = len(A)
        for i in range(n):
            if A[i] < 0:
                A[i] = 0
            else:
                A[i] = 1
        for i in range(1, len(A)):
            A[i] = A[i-1] + A[i]
        c = []
        for i in range(len(B)):
            l = B[i][0]
            r = B[i][1]
            summ = 0
            if l == 0:
                summ = A[r]
            else:
                summ = A[r] - A[l-1]
            c.append(summ)
        return c 
