Check Pair Sum

Problem Description
Given an Array of integers B, and a target sum A.
Check if there exists a pair (i,j) such that Bi + Bj = A and i!=j.

Problem Constraints
1 <= Length of array B <= 105
0 <= Bi <= 109
0 <= A <= 109

Input Format
First argument A is the Target sum, and second argument is the array B

Output Format
Return an integer value 1 if there exists such pair, else return 0.

Example Input
Input 1:
A = 8   
B = [3, 5, 1, 2, 1, 2]
Input 2:
A = 21   
B = [9, 10, 7, 10, 9, 1, 5, 1, 5]

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Example 1:
It is possible to obtain sum 8 using 3 and 5.
Example 2:
There is no such pair exists.

CODE:

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def check_pair_sum(self, A, B):
        hm = {}
        for i in range(len(B)):
            if B[i] in hm:
                hm[B[i]] += 1
            else:
                hm[B[i]] = 1

        for i in range(len(B)):
            if A-B[i] == B[i]:
                if hm[B[i]] >= 2:
                    return 1
            elif A-B[i] in hm:
                return 1
        return 0

'or'

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def check_pair_sum(self, A, B):
        hs = set()
        ans = 0
        for i in range(len(B)):
            if A - B[i] in hs:
                return 1
            hs.add(B[i])
        return 0


solution = Solution()
print(solution.check_pair_sum( B = [3, 5, 1, 2, 1, 2] ))  -->  O/P: 1
print(solution.check_pair_sum( B = [9, 10, 7, 10, 9, 1, 5, 1, 5] ))  -->  O/P: 0
