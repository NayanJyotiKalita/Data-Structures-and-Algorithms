Count Increasing Triplets

Problem Description
You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]

Problem Constraints
1 <= N <= 103
1 <= A[i] <= 109

Input Format
First argument A is an array of integers.

Output Format
Return an integer.

Example Input
Input 1:
A = [1, 2, 4, 3]
Input 2:
A = [2, 1, 2, 3]

Example Output
Output 1:
2
Output 2:
1

Example Explanation
For Input 1:
The triplets that satisfy the conditions are [1, 2, 3] and [1, 2, 4].
For Input 2:
The triplet that satisfy the conditions is [1, 2, 3].

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def count_increasing_triplets(self, A):
        ans = 0
        n = len(A)
        for i in range(1, n-1):
            left = 0
            right = 0
            prod = 0
            for j in range(i-1, -1, -1):
                if A[j] < A[i]:
                    left += 1
            for j in range(i+1, n):
                if A[j] > A[i]:
                    right += 1
            prod = left * right
            # print(prod)
            ans += prod
            # print(ans)
        return ans
