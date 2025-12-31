# Minimum Difference

Problem Description

You are given a 2-D matrix C of size A × B.
You need to build a new 1-D array of size A by taking one element from each row of the 2-D matrix in such a way that the cost of the newly built array is minimized.

The cost of an array is the minimum possible value of the absolute difference between any two adjacent elements of the array.

So if the newly built array is X, the element picked from row 1 will become X[1], element picked from row 2 will become X[2], and so on.

Determine the minimum cost of the newly built array.



Problem Constraints

2 <= A <= 1000
2 <= B <= 1000
1 <= C[i][j] <= 106



Input Format

The first argument is an integer A denoting number of rows in the 2-D array.
The second argument is an integer B denoting number of columns in the 2-D array.
The third argument is a 2-D array C of size A x B.



Output Format

Return an integer denoting the minimum cost of the newly build array.



Example Input

Input 1:

 A = 2
 B = 2
 C = [ [8, 4]
      [6, 8] ]
Input 2:

 A = 3
 B = 2
 C = [ [7, 3]
       [2, 1]
       [4, 9] ]


Example Output

Output 1:

 0
Output 2:

 1


Example Explanation

Explanation 1:

 Newly build array : [8, 8]. The minimum cost will be 0 since the absolute difference will be 0(8-8).
Explanation 2:

 Newly build array : [3, 2, 4]. The minimum cost will be 1 since the minimum absolute difference will be 1(3 - 2).

 # CODE

 class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        for i in range(len(C)):
            C[i].sort()
        #print(C)
        ans = 10**9

        for i in range(A-1):
            for j in range(B):
                min_diff = float('inf')
                for k in range(B):
                    diff = abs(C[i][j] - C[i + 1][k])
                    min_diff = min(min_diff, diff)
                ans = min(ans, min_diff)
        
        return ans

or
    
    def solve(self, A, B, C):
        for row in C:
            row.sort()

        ans = float('inf')
        for i in range(A - 1):
            p1, p2 = 0, 0
            while p1 < B and p2 < B:
                diff = abs(C[i][p1] - C[i+1][p2])
                ans = min(ans, diff)
                if C[i][p1] < C[i+1][p2]:
                    p1 += 1
                else:
                    p2 += 1

        return ans

or

class Solution:
    def binary\_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left if left < len(arr) else right

    def solve(self, A, B, C):
        for row in C:
            row.sort()

        ans = float('inf')
        for i in range(A - 1):
            for j in range(B):
                idx = self.binary\_search(C[i+1], C[i][j])
                diff = abs(C[i][j] - C[i+1][idx])
                if idx > 0:
                    diff = min(diff, abs(C[i][j] - C[i+1][idx-1]))
                ans = min(ans, diff)

        return ans
