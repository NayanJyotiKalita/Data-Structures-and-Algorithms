Subarray with least average

Problem Description
Given an array A of size N, find the subarray of size B with the least average.

Problem Constraints
1 <= B <= N <= 105
-105 <= A[i] <= 105

Input Format
First argument contains an array A of integers of size N.
Second argument contains integer B.

Output Format
Return the index of the first element of the subarray of size B that has least average.
Array indexing starts from 0.
 
Example Input
Input 1:
A = [3, 7, 90, 20, 10, 50, 40]
B = 3
Input 2:
A = [3, 7, 5, 20, -10, 0, 12]
B = 2

Example Output
Output 1:
3
Output 2:
4

Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.
Explanation 2:
Subarray between [4, 5] has minimum average

CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def subarray_with_least_average(self, A, B):

        idx = 0
        n = len(A)
        ans = 1000000
        summ = 0

        for i in range(B):
            summ += A[i]
        ans = min(ans, summ)

        i = 1
        j = B
        while j < n:
            summ += A[j] - A[i-1]
            if summ < ans:
                ans = summ
                idx = i
            i += 1
            j += 1

        return idx


solution = Solution()
print(solutiom.subarray_with_least_average(A = [3, 7, 5, 20, -10, 0, 12], B = 2))  -->  O/P: 4
