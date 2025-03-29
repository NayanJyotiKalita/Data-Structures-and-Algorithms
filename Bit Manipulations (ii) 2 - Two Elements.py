Two Elements

Problem Description
Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
Find the two integers that appear only once.
Note: Return the two numbers in ascending order.

Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109

Input Format
The first argument is an array of integers of size N.

Output Format
Return an array of two integers that appear only once.

Example Input
Input 1:
A = [1, 2, 3, 1, 2, 4]
Input 2:
A = [1, 2]

Example Output
Output 1:
[3, 4]
Output 2:
[1, 2]

Example Explanation
Explanation 1:
3 and 4 appear only once.
Explanation 2:
1 and 2 appear only once.

CODE:

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def two_elements(self, A):
        xor = 0
        ans1 = 0
        ans2 = 0

        n = len(A)
        for i in range(n):
            xor = xor ^ A[i]

        position = -1
        for i in range(32):
            if (xor & (1 << i)) > 0:
                position = i
                break

        for i in range(n):
            if (A[i] & (1 << position)) > 0:
                ans1 = ans1 ^ A[i]  
            else:
                ans2 = ans2 ^ A[i]
                
        if ans1 > ans2:
            return ans2,ans1
        else:
            return ans1,ans2


solution = Solution()
print(solution.two_elements( A = [1, 2, 3, 1, 2, 4] ))
