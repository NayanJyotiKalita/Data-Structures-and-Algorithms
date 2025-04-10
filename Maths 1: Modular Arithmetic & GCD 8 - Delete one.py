Delete One

Problem Description
Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.
Find the maximum value of GCD.

Problem Constraints
2 <= N <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the maximum value of GCD.

Example Input
Input 1:
 A = [12, 15, 18]
Input 2:
 A = [5, 15, 30]

Example Output
Output 1:
 6
Output 2:
 15

Example Explanation
Explanation 1:
 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum value of gcd is 6.
Explanation 2:
 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.
 Maximum value of gcd is 15.

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def delete_one(self, A):

        n = len(A)

        pgcd = [0] * n
        pgcd[0] = A[0]
        for i in range(1, n):
            pgcd[i] = self.gcd(pgcd[i-1], A[i])

        sgcd = [0] * n
        sgcd[n-1] = A[n-1]
        for i in range(n-2, -1, -1):
            sgcd[i] = self.gcd(sgcd[i+1], A[i])

        ans = 0
        for i in range(n):
            if i == 0:
                ans = max(ans, sgcd[i+1])
            elif i == n-1:
                ans = max(ans, pgcd[i-1])
            else:
                ans = max(ans, self.gcd(pgcd[i-1], sgcd[i+1]))
        return ans

    def gcd(self, A, B):
        if B == 0:
            return A
        return self.gcd(B, A % B)


solution = Solution()
print(solution.delete_one( A = [12, 15, 18] ))  -->  O/P: 6
