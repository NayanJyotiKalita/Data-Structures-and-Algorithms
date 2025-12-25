# Median of two sorted arrays

Problem Description

Given two sorted arrays A and B of size M and N respectively, return the median of the two sorted arrays.
Round of the value to the floor integer [2.6=2, 2.2=2]


Problem Constraints

0 <= M <= 105
0 <= N <= 105
-109 <= A[i], B[i] <= 109


Input Format

First argument A is an array of integers.
First argument B is an array of integers.


Output Format

Return an integer.


Example Input

Input 1:
A = [5, 7]
B = [6]
Input 2:
A = [1, 2]
B = [3, 4]


Example Output

Output 1:
6
Output 2:
2


Example Explanation

Example 1:
merged array = [5, 6, 7] and median is 6.
Example 2:
merged array = [1, 2, 3, 4] and median is 
(2 + 3) / 2 = 2.5 
            = floor(2.5) 
            = 2


# CODE

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        if len(A) > len(B):
            return self.solve(B, A)

        n1, n2 = len(A), len(B)
        N = n1 + n2
        start, end = 0, n1

        while start <= end:
            cut1 = (start + end) // 2
            cut2 = N // 2 - cut1

            l1 = float('-inf') if cut1 == 0 else A[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else B[cut2 - 1]
            r1 = float('inf') if cut1 == n1 else A[cut1]
            r2 = float('inf') if cut2 == n2 else B[cut2]

            # Check if partition is correct
            if l1 <= r2 and l2 <= r1:
                # If total length is odd, return the middle element
                if N % 2 == 1:
                    return math.floor(min(r1, r2))
                # If total length is even, return the average of the two middle elements
                else:
                    return math.floor((max(l1, l2) + min(r1, r2)) / 2)

            elif l1 > r2:
                end = cut1 - 1
            else:
                start = cut1 + 1

        return 0
