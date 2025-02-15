Generate all subarrays

Problem Description
You are given an array A of N integers.
Return a 2D array consisting of all the subarrays of the array

Note : The order of the subarrays in the resulting 2D array does not matter.

Problem Constraints
1 <= N <= 100
1 <= A[i] <= 105

Input Format
First argument A is an array of integers.

Output Format
Return a 2D array of integers in any order.

Example Input
Input 1:
A = [1, 2, 3]
Input 2:
A = [5, 2, 1, 4]

Example Output
Output 1:
[[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
Output 2:
[[1 ], [1 4 ], [2 ], [2 1 ], [2 1 4 ], [4 ], [5 ], [5 2 ], [5 2 1 ], [5 2 1 4 ] ]

CODE:

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def all_subarrays(self, A):
        ans = []
        n = len(A)
        for si in range(n):
            for ei in range(si, n):
                ls = []
                for k in range(si, ei + 1):
                    ls.append(A[k])
                ans.append(ls)
        return ans
        
'or'

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def all_subarrays(self, A):
        ans = []
        for si in range(0, len(A)):
            for ei in range(si, len(A)):
                ans.append(A[si:ei+1])
        return ans

solution = Solution()
print(solution.all_subarrays(A = [5, 2, 1, 4]))
