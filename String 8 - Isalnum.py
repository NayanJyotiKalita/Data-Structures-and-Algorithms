Isalnum()

Problem Description
You are given a function isalpha() consisting of a character array A.
Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.

Problem Constraints
1 <= |A| <= 105

Input Format
Only argument is a character array A.

Output Format
Return 1 if all the characters of the character array are alphanumeric (a-z, A-Z and 0-9), else return 0.

Example Input
Input 1:
 A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
Input 2:
 A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 All the characters are alphanumeric.
Explanation 2:
 All the characters are NOT alphabets i.e ('#').

CODE:

class Solution:
    # @param A : list of characters
    # @return an integer
    def isalnum(self, A):
        for i in A:
            if not i.isalnum():
                return 0
        return 1

or

class Solution:
    # @param A : list of characters
    # @return an integer
    def isalnum(self, A):
        for i in A:
            if not ( (ord(i) >= 65 and ord(i) <= 90 ) or (ord(i) >= 97 and ord(i) <= 122 ) or ( ord(i) >= 48 and ord(i) <= 57 ) )  :
                return 0
        return 1

or 

class Solution:
    # @param A : list of characters
    # @return an integer
    def isalnum(self, A):
        for x in A:
            if x >= 'a' and x <= 'z':
                continue
            if x >= 'A' and x <= 'Z':
                continue
            if x >= '0' and x <= '9':
                continue
            return 0
        return 1


solution = Solution()
print(solution.isalnum(A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']))
