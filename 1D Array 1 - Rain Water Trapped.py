Rain Water Trapped

Problem Description
Imagine a histogram where the bars' heights are given by the array A. Each bar is of uniform width, which is 1 unit. When it rains, water will accumulate in the valleys between the bars.
Your task is to calculate the total amount of water that can be trapped in these valleys.

Example:
The Array A = [5, 4, 1, 4, 3, 2, 7] is visualized as below. The total amount of rain water trapped in A is 11.

Problem Constraints
1 <= |A| <= 105
0 <= A[i] <= 105

Input Format
First and only argument is the Integer Array, A.

Output Format
Return an Integer, denoting the total amount of water that can be trapped in these valleys

Example Input
Input 1:
 A = [0, 1, 0, 2]
Input 2:
A = [1, 2]

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:
1 unit is trapped on top of the 3rd element.
Rain Water Histogram
Explanation 2:
No water is trapped.

CODE:

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
        n = len(A)

        max_left = [0] * n
        max_left[0] = A[0]
        max_right = [0] * n
        max_right[-1] = A[-1]

        for i in range(1, n):
            max_left[i] = max(A[i], max_left[i - 1])
        
        for i in range(n - 2, -1, -1):
            max_right[i] = max(A[i], max_right[i + 1])

        total = 0
        for i in range(n):
            total += min(max_left[i], max_right[i]) - A[i]
        
        return total

solution = Solution()
print(solution.trap(A = [0, 1, 0, 2]))
