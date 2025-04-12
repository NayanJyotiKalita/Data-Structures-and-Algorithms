Sub-array with 0 sum

Problem Description
Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
If the given array contains a sub-array with sum zero return 1, else return 0.

Problem Constraints
1 <= |A| <= 100000
-10^9 <= A[i] <= 10^9

Input Format
The only argument given is the integer array A.

Output Format
Return whether the given array contains a subarray with a sum equal to 0.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [4, -1, 1]

Example Output
Output 1:
 0
Output 2:
 1

Example Explanation
Explanation 1:
 No subarray has sum 0.
Explanation 2:
 The subarray [-1, 1] has sum 0.

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def subarray_with_0_sum(self, A):
        summ = 0
        hm = {}
        for i in range(len(A)):
            summ += A[i]
            if summ in hm:
                return 1
            elif summ == 0:
                return 1
            
            if summ in hm:
                hm[summ] += 1
            else:
                hm[summ] = 1
        
        return 0


solution = Solution()
print(solution.subarray_with_0_sum( A = [1, 2, 3, 4, 5] ))  -->  O/P: 0
print(solution.subarray_with_0_sum( A = [4, -1, 1] )) --> O/P: 1
