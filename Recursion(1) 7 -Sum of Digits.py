Sum of Digits

Problem Description
Given a number A, we need to find the sum of its digits using recursion.

Problem Constraints
1 <= A <= 109

Input Format
The first and only argument is an integer A.

Output Format
Return an integer denoting the sum of digits of the number A.

Example Input
Input 1:
 A = 46
Input 2:
 A = 11

Example Output
Output 1:
 10
Output 2:
 2

Example Explanation
Explanation 1:
 Sum of digits of 46 = 4 + 6 = 10
Explanation 2:
 Sum of digits of 11 = 1 + 1 = 2

CODE:

class Solution:
    # @param A : integer
    # @return an integer
    def sum_of_digits(self, A):
        if A == 0:
            return A % 10
        return A % 10 + self.solve(A // 10)


solution = Solution()
print(solution.sum_of_digits( A = 46 ))  --> O/P: 10
