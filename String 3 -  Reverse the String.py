Reverse the String

Problem Description
You are given a string A of size N.

Return the string A after reversing the string word by word.
NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

Problem Constraints
1 <= N <= 3 * 105

Input Format
The only argument given is string A.

Output Format
Return the string A after reversing the string word by word.

Example Input
Input 1:
A = "the sky is blue"
Input 2:
A = "this is ib"

Example Output
Output 1:
"blue is sky the"
Output 2:
"ib is this"    

Example Explanation
Explanation 1:
We reverse the string word by word so the string becomes "blue is sky the".
Explanation 2:
We reverse the string word by word so the string becomes "ib is this".

CODE:

class Solution:
    # @param A : string
    # @return a strings
    def reverse_string(self, A):
        a = A.split()
        return " ".join(a[::-1])


solution = Solution()
print(solution.reverse_string(A = "the sky is blue"))  -->  O/P: "blue is sky the"
