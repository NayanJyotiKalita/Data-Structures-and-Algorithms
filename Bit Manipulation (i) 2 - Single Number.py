Single Number

Problem Description
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.
NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Problem Constraints
1 <= |A| <= 2000000
0 <= A[i] <= INTMAX

Input Format
The first and only argument of input contains an integer array A.

Output Format
Return a single integer denoting the single element.

Example Input
Input 1:
 A = [1, 2, 2, 3, 1]
Input 2:
 A = [1, 2, 2]

Example Output
Output 1:
 3
Output 2:
 1

Example Explanation
Explanation 1:
3 occurs once.
Explanation 2:
1 occurs once.

CODE:

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in range(len(A)):
            ans = ans ^ A[i]
        return ans

'or'

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in range(32):
            count = 0
            for j in range(len(A)):
                if (A[j] & (1 << i)) > 0:
                    count += 1
            if count & 1 == 1:
                ans = ans | (1 << i)
        return ans


solution = Solution()
print(solution.singleNumber( A = [1, 2, 2, 3, 1] ))
