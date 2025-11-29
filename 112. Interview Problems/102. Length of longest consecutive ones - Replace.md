Length of longest consecutive ones (Replace)

Given a binary string A. It is allowed to do at most one replacement of 0 by 1. Find and return the length of the longest consecutive 1’s that can be achieved.
'or'
Given a binary string A. We can almost replace a single 0 with 1. Find the maximum consecutive 1's we can get in the string after the replacement.

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
    4

Input 2:
    A = "111011101"
Output 2:
    7

CODE:

class Solution:
    def longest_consecutive_ones_replace(self, A):
          ans = 0
          n = len(A)
          for i in range(n):
                if A[i] == 0:
                      l, r, = 0, 0
                      j = i - 1
                      while j >= 0 and A[j] == 1:
                            l += 1
                            j -= 1
                      j = i + 1
                      while j < n and A[j] == 1:
                            r += 1
                            j += 1
                      ans = max(ans, l + r + 1)
          if ans == 0 and n > 0:
                ans = n
          return ans

solution = Solution()
print(solution.longest_consecutive_ones_replace(A = "111011101"))
