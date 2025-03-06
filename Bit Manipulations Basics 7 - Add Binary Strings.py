Add Binary Strings

Problem Description
Given two binary strings A and B. Return their sum (also a binary string).

Problem Constraints
1 <= length of A <= 105
1 <= length of B <= 105
A and B are binary strings

Input Format
The two argument A and B are binary strings.

Output Format
Return a binary string denoting the sum of A and B

Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"

Example Output
Output 1:
"111"
Output 2:
"1000"

Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:
The sum of 110 and 10 is 1000

CODE:

class Solution:
  	# @param A : string
  	# @param B : string
  	# @return a strings
  	def addBinary(self, A, B):
          carry=0
          i=len(A)-1
          j=len(B)-1
          final=""
          while(i>=0 or j>=0 or carry):
              s=0
              if i>=0:
                  s+=int(A[i])
                  i-=1
              if j>=0:
                  s+=int(B[j])
                  j-=1
              s+=carry
              ans=s%2
              carry=s//2
              final+=str(ans)
          return final[::-1]


solution = Solution()
print(solution.addBinary(A = "100", B = "11"))
