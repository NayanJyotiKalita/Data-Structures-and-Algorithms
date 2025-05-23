Counting Subarrays Easy

Problem Description
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.

Problem Constraints
1 <= N <= 5 x 103
1 <= A[i] <= 1000
1 <= B <= 107

Input Format
First argument is an integer array A.
Second argument is an integer B.

Output Format
Return an integer denoting the number of subarrays in A having sum less than B.

Example Input
Input 1:
 A = [2, 5, 6]
 B = 10
Input 2:
 A = [1, 11, 2, 3, 15]
 B = 10

Example Output
Output 1:
 4
Output 2:
 4

Example Explanation
Explanation 1:
 The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},
Explanation 2:
 The subarrays with sum less than B are {1}, {2}, {3} and {2, 3}

CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def counting_subarrays(self, A, B):
        count = 0
        for i in range(1, len(A)):
            A[i] = A[i-1] + A[i]
        n = len(A)
        for si in range(n):
            summ = 0
            for ei in range(si, n):
                if si == 0:
                    summ = A[ei]
                else:
                    summ = A[ei] - A[si - 1]
                if summ < B:
                    count += 1
        return count
     
'or'

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def counting_subarrays(self, A, B):
        count = 0
        for si in range(len(A)):
            carrysum = 0
            for ei in range(si, len(A)):
                carrysum += A[ei]
                if carrysum < B:
                    count += 1
        return count

solution = Solution()
print(solution.counting_subarrays(A = [1, 11, 2, 3, 15], B = 10))  -->  O/P: 4
