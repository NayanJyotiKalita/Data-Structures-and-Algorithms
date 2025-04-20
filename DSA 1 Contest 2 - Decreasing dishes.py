Decreasing dishes

Problem Description
Given an array of N positive integers representing the weights of ingredients in a dish.
Find the maximum possible sum of a subarray with decreasing weights.

Problem Constraints
1 <= N <= 105
0 <= A[i] <= 105
Sum of all elements of A <= 109

Input Format
First argument A is an array of integers.

Output Format
Return an integer denoting maximum possible sum of a subarray with decreasing weights.

Example Input
Input 1:
A = [3, 2, 1] 
Input 2:
A = [3, 3, 5, 0, 1]

Example Output
Output 1:
6
Output 2:
5

Example Explanation
Example 1:
We can take the subarray indexed [0-2] which are in decreasing order the sum the elements are 3+2+1=6.
Example 2:
We can take the subarray indexed [2-3] which are in decreasing order the sum of the elements are 5+0=5.

CODE:

 class Solution:
    # @param A : list of integers
    # @return an integer
    def decreasing_dishes(self, A):
        ans = 0
        curr_sum = A[0]
        
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                curr_sum += A[i]
            else:
                ans = max(ans, curr_sum)
                curr_sum = A[i]
        
        ans = max(ans, curr_sum)
        return ans 


solution = Solution()
print(solution.decreasing_dishes( A = [3, 2, 1] ))  -->  O/P: 6
