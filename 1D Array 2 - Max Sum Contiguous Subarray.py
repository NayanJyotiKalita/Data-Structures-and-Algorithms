Max Sun Contiguous Subarray

Problem Description
Find the maximum sum of contiguous non-empty subarray within an array A of length N.

Problem Constraints
1 <= N <= 10^6
-1000 <= A[i] <= 1000

Input Format
The first and the only argument contains an integer array, A.

Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.

Example Input
Input 1:
 A = [1, 2, 3, 4, -10] 
Input 2:
 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 

Example Output
Output 1:
 10 
Output 2:
 6 

Example Explanation
Explanation 1:
 The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
Explanation 2:
 The subarray [4,-1,2,1] has the maximum possible sum of 6. 

CODE:

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        current_sum = 0
        max_sum = -10**9
        for i in range(len(A)):
            current_sum = A[i] + max(current_sum, 0)
            max_sum = max(max_sum, current_sum)
        return max_sum


solution = Solution()
print(solution.maxSubArray(A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
