Heads and Tails

Problem Description
You are given a binary string A of length N, which represents the results of a series of coin tosses. 0 represents tails and 1 represents heads. You want to
find the length of the longest streak of consecutive heads.

Problem Constraints
1 <= N <= 105
String A contains only characters '0' and '1'.

Input Format
Only argument is a string A.

Output Format
Return an integer denoting the length of the longest streak of consecutive heads.

Example Input
Input 1:
A = "101110"
Input 2:
A = "110101"

Example Output
Output 1:
3
Output 2:
2

Example Explanation
Explanation 1:
The longest streak of consecutive head in A is = "101110" is highlighted.
Explanation 2:
The longest streak of consecutive head in A is = "110101" is highlighted.

CODE:

 class Solution:
    # @param A : string
    # @return an integer
    def head_tail(self, A):
        ans = 0
        count = 0
        for i in range(len(A)):
            if A[i] == '1':
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        return ans
