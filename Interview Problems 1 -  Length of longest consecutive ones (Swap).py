Length of longest consecutive ones (Swap)

Problem Description:
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.
  
Input Format
The only argument given is string A.

Output Format
Return the length of the longest consecutive 1’s that can be achieved.
  
Constraints
1 <= length of string <= 1000000
A contains only characters 0 and 1.

For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7

CODE:

class Solution:
    # @param A : string
    # @return an integer
    def longest_consecutive_ones_swap(self, A):
        ans = 0
        total_Ones = 0
        for i in range(len(A)):
            if A[i] == '0':
                l, r = 0, 0
                j = i - 1
                while j >= 0 and A[j] == '1':
                    l += 1
                    j -= 1
                j = i + 1
                while j < len(A) and A[j] == '1':
                    r += 1
                    j += 1
                ans = max(ans, l + r)
            else:
                total_Ones += 1
        
        if total_Ones == len(A):
            return len(A)
        if ans < total_Ones:
            return ans + 1
        return ans

solution = Solution()
print(solution.longest_consecutive_ones_swap(A = "111000"))
