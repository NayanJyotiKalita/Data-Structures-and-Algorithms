Range divisibility

Problem Description
Samantha is a teacher who is teaching a group of students about divisibility by 7. To make the lesson more interesting, she gives them an array A of size N and asks them Q queries given by B.
In each query, she gives them a range from L to R given by B[i][0] and B[i][1] and asks them to find the count of numbers divisible by 7 in subarray A[L], A[L+1], ... A[R]. Since some students are struggling to solve the problem, Samantha asks for your help to come up with a solution.

Problem Constraints
1 <= N <= 105
1 <= Q <= 105
1 <= A[i] <= 109
0 <= B[i][0], B[i][1] < N

Input Format
First argument A is an integer array.
Second argument B is a 2D integer array.

Output Format
Return an integer array where ith index contains the count of numbers divisible by 7 in the range A[B[i][0]] to A[B[i][1]].

Example Input
Input 1:
A = [2, 7, 14, 5, 7]
B = [[0, 2], [2, 4]]
Input 2:
A = [7, 14, 2, 14]
B = [[1, 2], [0, 3]]

Example Output
Output 1:
[2, 2]
Output 2:
[1, 3]

Example Explanation
Explanation 1:
The subarray for the first query is [2, 7, 14]. The numbers divisible by 7 are 7 and 14.
The subarray for the second query is [14, 5, 7]. The numbers divisible by 7 are 14 and 7.
Explanation 2:
The subarray for the first query is [14, 2]. The number divisible by 7 is 14.
The subarray for the second query is [7, 14, 2, 14]. The numbers divisible by 7 are 7, 14 and 14.


CODE:

 class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def range_divisibility(self, A, B):
        for i in range(len(A)):
            if A[i] % 7 == 0:
                A[i] = 1
            else:
                A[i] = 0
        n = len(A)
        for i in range(1, n):
            A[i] = A[i-1] + A[i]
        n = len(A)
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
