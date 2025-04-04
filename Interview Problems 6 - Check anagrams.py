Check anagrams

Problem Description
You are given two lowercase strings A and B each of length N. Return 1 if they are anagrams to each other and 0 if not.
Note : Two strings A and B are called anagrams to each other if A can be formed after rearranging the letters of B.

Problem Constraints
1 <= N <= 105
A and B are lowercase strings

Input Format
Both arguments A and B are a string.

Output Format
Return 1 if they are anagrams and 0 if not

Example Input
Input 1:
A = "cat"
B = "bat"
Input 2:
A = "secure"
B = "rescue"

Example Output
Output 1:
0
Output 2:
1

Example Explanation
For Input 1:
The words cannot be rearranged to form the same word. So, they are not anagrams.
For Input 2:
They are an anagram.

CODE:

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def check_anagrams(self, A, B):
        a = list(A)
        b = list(B)
        a.sort()
        b.sort()
        if a == b:
            return 1
        else:
            return 0

or

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def check_anagrams(self, A, B):
        counter = [0] * 26
        for i in A:
            counter[ord(i) - ord("a")] += 1
        for i in B:
            counter[ord(i) - ord("a")] -= 1
        
        for i in counter:
            if i != 0:
                return 0
        return 1


solution = Solution()
print(solution.check_anagrams( A = "secure", B = "rescue" ))
