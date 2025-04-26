Count Occurrences

Problem Description
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.

Problem Constraints
1 <= |A| <= 1000

Input Format
The first and only argument contains the string A, consisting of lowercase English alphabets.

Output Format
Return an integer containing the answer.

Example Input
Input 1:
  abobc
Input 2:
  bobob

Example Output
Output 1:
  1
Output 2:
  2

Example Explanation
Explanation 1:
  The only occurrence is at second position.
Explanation 2:
  Bob occures at first and third position.

CODE:

class Solution:
    # @param A : string
    # @return an integer
    def count_occurences(self, A):
        count = 0
        n = len(A)
        for i in range(n):
            for j in range(i+2, n):
                if A[i:j+1] == 'bob':
                    count += 1
        return count

or 

class Solution:
    # @param A : string
    # @return an integer
    def count_occurences(self, A):
        s = A
        prev = -1
        ans = 0
        cur = s.find("bob", prev+1)
        while cur != -1:
            ans += 1
            prev = cur
            cur = s.find("bob", prev+1)
        return ans


solution = Solution()
print(solution.count_occurences(A = 'abobc'))  -->  O/P: 1
print(solution.count_occurences(A = 'bobob'))  -->  O/P: 2
