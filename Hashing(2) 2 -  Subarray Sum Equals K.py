Subarray Sum Equals K

Problem Description
Given an array of integers A and an integer B.
Find the total number of subarrays having sum equals to B.

Problem Constraints
 1 <= length of the array <= 50000
-1000 <= A[i] <= 1000

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the total number of subarrays having sum equals to B.

Example Input
Input 1:
A = [1, 0, 1]
B = 1
Input 2:
A = [0, 0, 0]
B = 0

Example Output
Output 1:
4
Output 2:
6

Example Explanation
Explanation 1:
[1], [1, 0], [0, 1] and [1] are four subarrays having sum 1.
Explanation 1:
All the possible subarrays having sum 0.

CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def subarray_sum_equal_k(self, A, B):
        hm = {}
        summ = 0
        count = 0
        for i in range(len(A)):
            
            summ += A[i]
            if summ - B == 0:
                count += 1
            if summ - B in hm:
                count += hm[summ - B]
            
            if summ in hm:
                hm[summ] += 1
            else:
                hm[summ] = 1
        
        return count


solution = Solution()
print(solution.subarray_sum_equal_k( A = [1, 0, 1], B = 1 ))  -->  O/P: 4
print(solution.subarray_sum_equal_k( A = [0, 0, 0], B = 0 ))  -->  O/P: 6
