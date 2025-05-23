Longest Subarray Zero Sum

Problem Description
Given an array A of N integers.
Find the length of the longest subarray in the array which sums to zero.
If there is no subarray which sums to zero then return 0.

Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Input Format
Single argument which is an integer array A.

Output Format
Return an integer.

Example Input
Input 1:
 A = [1, -2, 1, 2]
Input 2:
 A = [3, 2, -1]

Example Output
Output 1:
3
Output 2:
0

Example Explanation
Explanation 1:
 [1, -2, 1] is the largest subarray which sums up to 0.
Explanation 2:
 No subarray sums up to 0.

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def longest_subarray_0_sum(self, A):
        ans = 0
        summ = 0
        hm = {0 : -1}
        for i in range(len(A)):
            summ += A[i]
            if summ in hm:
                ans = max(ans, i - hm[summ])
            else:
                hm[summ] = i
        
        if ans > 0:
            return ans
        return 0

'or'

class Solution:
    # @param A : list of integers
    # @return an integer
    def longest_subarray_0_sum(self, A):
        pref = {}
        curr = 0
        pref[0] = 0
        ans = 0
        
        for i in range(1,len(A) + 1):

            curr += A[i - 1]
            if curr in pref:
                ans = max(ans, i - pref[curr])
            else:
                pref[curr] = i
        return ans


solution = Solution()
print(solution.longest_subarray_0_sum( A = [1, -2, 1, 2] ))  -->  O/P: 3
print(solution.longest_subarray_0_sum( A = [3, 2, -1] ))  -->  O/P: 0
