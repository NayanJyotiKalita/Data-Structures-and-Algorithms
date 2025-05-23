Factors sort

Problem Description
You are given an array A of N elements. Sort the given array in increasing order of number of distinct factors of each element, i.e., element having the least number of factors 
should be the first to be displayed and the number having highest number of factors should be the last one. If 2 elements have same number of factors, then number with less value should come first.
Note: You cannot use any extra space

Problem Constraints
1 <= N <= 104
1 <= A[i] <= 104

Input Format
First argument A is an array of integers.

Output Format
Return an array of integers.

Example Input
Input 1:
A = [6, 8, 9]
Input 2:
A = [2, 4, 7]

Example Output
Output 1:
[9, 6, 8]
Output 2:
[2, 7, 4]

Example Explanation
For Input 1:
The number 9 has 3 factors, 6 has 4 factors and 8 has 4 factors.
For Input 2:
The number 2 has 2 factors, 7 has 2 factors and 4 has 3 factors.

CODE:

import functools
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def factors_sort(self, A):
        A = sorted(A, key = functools.cmp_to_key(self.compare))
        return A
    
    def compare(self, v1, v2):
        if self.factors(v1) == self.factors(v2):
            return v1 - v2
        else:
            return self.factors(v1) - self.factors(v2)
        
    def factors(self, n):
        cnt = 0
        i = 1
        while i*i <= n:
            if n % i == 0:
                cnt += (1 if i == n//i else 2)
            i += 1
        return cnt


solution = Solution()
print(solution.factors_sort( A = [6, 8, 9] ))  -->  O/P: [9, 6, 8]
