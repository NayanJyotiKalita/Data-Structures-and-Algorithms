Special Subsequences "AG" - 2


Problem Description
You have given a string A having Uppercase English letters.
You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.

Problem Constraints
1 <= length(A) <= 105

Input Format
First and only argument is a string A.

Output Format
Return an long integer denoting the answer.

Example Input
Input 1:
 A = "ABCGAG"
Input 2:
 A = "GAB"

Example Output
Output 1:
 3
Output 2:
 0

Example Explanation
Explanation 1:
 Subsequence "AG" is 3 times in given string, the pairs are (0, 3), (0, 5) and (4, 5). 
Explanation 2:
 There is no subsequence "AG" in the given string.

 CODE:

 class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        countA = 0
        count = 0
        for i in range(len(A)):
            if A[i] == 'A':
                countA += 1
            if A[i] == 'G':
                count += countA
        return count

solution = Solution()
