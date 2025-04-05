Fast Power

Problem Description
Given two positive integers A and B. Implement Fast Power function to compute AB
Note : Please use the approach taught in the class.

Problem Constraints
AB would fit in 64-bit type integer.

Input Format
Two integers A and B

Output Format
Single integer denoting the answer to AB

Example Input
Input 1 :
A = 2 , B = 10
Input 2 :
A = 1 , B = 100000000

Example Output
Output 1 :
1024
Output 2 :
1

Example Explanation
For Input 1 :
210 = 25 * 25 
25 = 32, so 32 * 32 = 1024
For Input 2 :
1 raised to power anything is 1

CODE:

class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def power(self, A, B):
        if A == 1:
            return A
        if B == 0:
            return 1
        half = self.power(A, B//2)
        if B % 2 == 0:
            return half * half
        else:
            return half * half * A


solution = Solution()
print(solution.power( A = 2 , B = 10 ))  -->  O/P: 1024
