Simple Reverse

Problem Description
Given a string A, you are asked to reverse the string and return the reversed string.

Problem Constraints
1 <= |A| <= 105
String A consist only of lowercase characters.

Input Format
First and only argument is a string A.

Output Format
Return a string denoting the reversed string.

Example Input
Input 1:
 A = scaler
Input 2:
 A = academy

Example Output
Output 1:
 relacs
Output 2:
 ymedaca

Example Explanation
Explanation 1:
 Reverse the given string.

CODE:

class Solution:
    # @param A : string
    # @return a strings
    def simple_reverse(self, A):
        a = list(A)
        a = a[::-1]
        return "".join(a)


solution = Solution()
print(solution.simple_reverse(A = 'scaler'))  -->  O/P: relacs
