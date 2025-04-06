Max of an Array Using Recursion

Problem Description
Given an array A of size N, write a recursive function that returns the maximum element of the array.

Problem Constraints
1 <= N <= 100
-1000 <= A[i] <= 1000

Input Format
The first line contains the array A.

Output Format
A single integer is the maximum value of the array.

Example Input
Input 1:
A = [12, 10, 3, 4, 5]
Input 2:
A = [1, -5, 80, -40]

Example Output
Output 1:
12
Output 2:
80

Example Explanation
Explanation 1:
 The Maximum element of the array A, [12, 10, 3, 4, 5] is 12
Explanation 2:
 The Maximum element of the array A, [1, -5, 80, -40] is 80

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def getMax(self, A):
        maxi = A[0]
        def maxiele(A, maxi, idx):
            if idx == len(A):
                return maxi
            if A[idx] > maxi:
                maxi = A[idx]
            return maxiele(A, maxi, idx + 1)
        return maxiele(A, A[0], 1)


solution = Solution()
print(solution.getMax( A = [12, 10, 3, 4, 5] ))  -->  O/P: 12
