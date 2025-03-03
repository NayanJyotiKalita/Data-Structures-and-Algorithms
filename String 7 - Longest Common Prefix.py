Longest Common Prefix

Problem Description
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.
The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Problem Constraints
0 <= sum of length of all strings <= 1000000

Input Format
The only argument given is an array of strings A.

Output Format
Return the longest common prefix of all strings in A.

Example Input
Input 1:
A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:
A = ["abab", "ab", "abcd"];

Example Output
Output 1:
"a"
Output 2:
"ab"

Example Explanation
Explanation 1:
Longest common prefix of all the strings is "a".
Explanation 2:
Longest common prefix of all the strings is "ab".

CODE:

class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        mini = min(A, key = len)
        ans = ""

        for i in range(len(mini)):
            isqualified = True
            ch = mini[i]

            for j in range(len(A)):
                if A[j][i] != ch:
                    return ans

            if isqualified:
                ans += ch
                
        return ans


solution = Solution()
print(solution.longestCommonPrefix(A = ["abcdefgh", "aefghijk", "abcefgh"]))
