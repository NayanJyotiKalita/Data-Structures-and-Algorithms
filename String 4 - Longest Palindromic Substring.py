Longest Palindromic Substring

Problem Description
Given a string A of size N, find and return the longest palindromic substring in A and its length.
Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
Incase of conflict, return the substring which occurs first ( with the least starting index).

Problem Constraints
1 <= N <= 6000

Input Format
First and only argument is a string A.

Output Format
Return a list consisting the longest palindromic substring of string A and its length.

Example Input
Input 1:
A = aaaabaaa
Input 2:
A = "abba"

Example Output
Output 1:
["aaabaaa", 7]
Output 2:
["abba", 4]

Example Explanation
Explanation 1:
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
Explanation 2:
We can see that longest palindromic substring is of length 4 and the string is "abba".

CODE:

class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
        B = []
        n = len(A)
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n:
                if A[l] != A[r]:
                    break
                if len(B) < (r - l + 1):
                    B = A[l : r + 1]
                l -= 1
                r += 1

        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n:
                if A[l] != A[r]:
                    break
                if len(B) < (r - l + 1):
                    B = A[l : r + 1]
                l -= 1
                r += 1

        return [''.join(B), len(B)]


solution = Solution()
print(solution.longestPalindrome(A = "aaaabaaa"))
