SUBARRAY OR

Problem Description
You are given an array of integers A of size N.
The value of a subarray is defined as BITWISE OR of all elements in it.
Return the sum of value of all subarrays of A % 109 + 7.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 108

Input Format
The first argument given is the integer array A.

Output Format
Return the sum of Value of all subarrays of A % 109 + 7.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [7, 8, 9, 10]

Example Output
Output 1:
 71
Output 2:
 110

Example Explanation

Explanation 1:
 Value([1]) = 1
 Value([1, 2]) = 3
 Value([1, 2, 3]) = 3
 Value([1, 2, 3, 4]) = 7
 Value([1, 2, 3, 4, 5]) = 7
 Value([2]) = 2
 Value([2, 3]) = 3
 Value([2, 3, 4]) = 7
 Value([2, 3, 4, 5]) = 7
 Value([3]) = 3
 Value([3, 4]) = 7
 Value([3, 4, 5]) = 7
 Value([4]) = 4
 Value([4, 5]) = 5
 Value([5]) = 5
 Sum of all these values = 71

Explanation 2:
 Sum of value of all subarray is 110.

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def subarray_or(self, A):

        ans = 0
        mod = 10**9 + 7
        n = len(A)
        ts = (n * (n + 1)) // 2  # ts = total_subbarray

        for i in range(32):
            x = 0
            contri_0 = 0
            for j in range(n):
                if A[j] & (1 << i) == 0:
                    x += 1
                else:
                    contri_0 += (x * (x + 1)) // 2
                    x = 0

            contri_0 += (x * (x + 1)) // 2
            contri_1 = ts - contri_0
            ans = (ans + (contri_1 * (1 << i)) % mod) % mod
        
        return ans


solution = Solution()
print(solution.subarray_or( A = [1, 2, 3, 4, 5] ))  -->  O/P: 71
