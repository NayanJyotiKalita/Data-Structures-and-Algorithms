Largest Number

Problem Description
Given an array A of non-negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109

Input Format
The first argument is an array of integers.

Output Format
Return a string representing the largest number.

Example Input
Input 1:
 A = [3, 30, 34, 5, 9]
Input 2:
 A = [2, 3, 9, 0]

Example Output
Output 1:
 "9534330"
Output 2:
 "9320"

Example Explanation
Explanation 1:
Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
Explanation 2:
Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.

CODE:

import functools
class Solution:
    # @param A : list of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(map(str,A))
        A = sorted(A, key = functools.cmp_to_key(self.compare))
        
        last =- 1
        for i in range(len(A)):     # done to dismiss the numbers where the array starts from 0
            if A[i] > '0':
                break
            last=i
        if last != -1 and A[len(A) - 1] == '0':
            return 0
        else:
            return "".join(A[last+1 : ])
        
    def compare(self, v1, v2):
        if v1+v2 > v2+v1:
            return -1
        elif v1+v2 < v2+v1:
            return 1
        else:
            return 0

'or'

import functools
class Solution:
    # @param A : list of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(map(str,A))
        # print(A)
        A = sorted(A, key = functools.cmp_to_key(self.compare))
        return "".join(A).lstrip('0') or "0"

    def compare(self, v1, v2):
        if v1+v2 > v2+v1:
            return -1
        elif v1+v2 < v2+v1:
            return 1
        else:
            return 0


solution = Solution()
print(solution.largestNumber(  A = [3, 30, 34, 5, 9] ))  -->  O/P: "9534330"
