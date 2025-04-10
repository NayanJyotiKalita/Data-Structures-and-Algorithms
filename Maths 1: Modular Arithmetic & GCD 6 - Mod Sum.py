Mod Sum

Problem Description
Given an array of integers A, calculate the sum of A [ i ] % A [ j ] for all possible i, j pairs. Return sum % (109 + 7) as an output.

Problem Constraints
1 <= length of the array A <= 105
1 <= A[i] <= 103

Input Format
The only argument given is the integer array A.

Output Format
Return a single integer denoting sum % (109 + 7).

Example Input
Input 1:
 A = [1, 2, 3]
Input 2:
 A = [17, 100, 11]

Example Output
Output 1:
 5
Output 2:
 61

Example Explanation
Explanation 1:
 (1 % 1) + (1 % 2) + (1 % 3) + (2 % 1) + (2 % 2) + (2 % 3) + (3 % 1) + (3 % 2) + (3 % 3) = 5

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def mod_sum(self, A):
        mod = 10**9 + 7
        freq = [0] * 1001

        for i in range(len(A)):
            freq[A[i]] += 1

        summ = 0
        for i in range(1, len(freq)):
            for j in range(1, len(freq)):
                val = i % j
                summ += ((val * freq[i] * freq[j]) % mod) % mod

        return summ


solution = Solution()
print(solution.mod_sum( A = [17, 100, 11] ))  -->  O/P: 61
