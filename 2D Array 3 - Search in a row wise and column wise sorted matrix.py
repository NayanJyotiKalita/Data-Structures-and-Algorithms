Search in a row wise and column wise sorted matrix

Problem Description
Given a matrix of integers A of size N x M and an integer B.

In the given matrix every row and column is sorted in non-decreasing order. Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.

Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.
Note 3: Expected time complexity is linear
Note 4: Use 1-based indexing

Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
-100000 <= B <= 100000

Input Format
The first argument given is the integer matrix A.
The second argument given is the integer B.

Output Format
Return the position of B and if it is not present in A return -1 instead.

Example Input
Input 1:-
A = [[1, 2, 3]
     [4, 5, 6]
     [7, 8, 9]]
B = 2
Input 2:-
A = [[1, 2]
     [3, 3]]
B = 3

Example Output
Output 1:-
1011
Output 2:-
2019

Example Explanation
Expanation 1:-
A[1][2] = 2
1 * 1009 + 2 = 1011
Explanation 2:-
A[2][1] = 3
2 * 1009 + 1 = 2019
A[2][2] = 3
2 * 1009 + 2 = 2020
The minimum value is 2019

CODE:

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def search_row_col_1009(self, A, B):
        n = len(A)
        m = len(A[0])
        i = 0
        j = m - 1
        ans = -1
        while i < n and j >= 0:
            if A[i][j] < B:
                i += 1
            elif A[i][j] > B:
                j -= 1
            else:
                while A[i][j] == B and j >= 0:
                    j -= 1
                    ans = (i + 1) * 1009 + (j + 2)
                break
        return ans

'or'

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def search_row_col_1009(self, A, B):
        n = len(A)
        m = len(A[0])
        i = 0
        j = m - 1
        found = -1
        
        while i < n and j >= 0:
            if A[i][j]  == B:
                found = True
                while j > 0:
                    #j -= 1
                    if A[i][j-1] != B:
                        #j += 1
                        break
                    else:
                        j -= 1
                break
            elif B > A[i][j]:
                i += 1
            else:
                j -= 1
        
        if found == -1:
            return -1
        else:
            return ((i+1) * 1009 + (j+1))


