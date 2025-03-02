Toggle Case

Problem Description
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.
You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.

Problem Constraints
1 <= N <= 105
A[i] ∈ ['a'-'z', 'A'-'Z']

Input Format
First and only argument is a character string A.

Output Format
Return a character string.

Example Input
Input 1:
 A = "Hello" 
Input 2:
 A = "tHiSiSaStRiNg" 

Example Output
Output 1:
 hELLO 
Output 2:
 ThIsIsAsTrInG 

Example Explanation
Explanation 1:
Hello changes to hELLO"
Explanation 2:
 "tHiSiSaStRiNg" changes to "ThIsIsAsTrInG"

CODE:

class Solution:
    # @param A : string
    # @return a strings
    def toggle_case(self, A):
        a = list(A)
        for i in range(len(a)):
            if ord(a[i]) >= 65 and ord(a[i]) <= 90:
                a[i] = chr(ord(A[i]) + 32)
            else:
                a[i] = chr(ord(A[i]) - 32)
        return ''.join(a)


solution = Solution()
print(solution.toggle_case(A = "tHiSiSaStRiNg")
