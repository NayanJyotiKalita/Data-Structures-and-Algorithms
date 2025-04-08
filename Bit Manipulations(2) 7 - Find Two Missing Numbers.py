Find Two Missing Numbers

Problem Description
Given an array A of length N where all the elements are distinct and are in the range [1, N+2].
Two numbers from the range [1, N+2] are missing from the array A. Find the two missing numbers.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= N+2
The elements of array A are distinct

Input Format
Only argument A is an array of integers

Output Format
Return a sorted array of size 2 denoting the missing elements.

Example Input
Input 1:
A = [3, 2, 4]
Input 2:
A = [5, 1, 3, 6]

Example Output
Output 1:
[1, 5]
Output 2:
[2, 4]

Example Explanation
For Input 1:
The missing numbers are 1 and 5.
For Input 2:
The missing numbers are 2 and 4.

CODE:

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def missing_num(self, A):

        n = len(A)
        XOR = 0

        for i in range(n):
            XOR ^= A[i]
            # print(XOR)
        for i in range(1, n + 3):
            XOR ^= i
            # print(XOR)

        rightmost_set_bit = XOR & ~(XOR-1)

        x, y = 0, 0
        for i in range(n):
            if (A[i] & rightmost_set_bit) > 0:
                x = x ^ A[i]  
            else:
                y = y ^ A[i]  
                
        for i in range(1, n + 3):
            if (i & rightmost_set_bit) > 0:
                x = x ^ i 
            else:
                y = y ^ i
                
        return [min(x, y), max(x, y)]


solution = Solution()
print(solution.missing_num( A = [5, 1, 3, 6] ))  -->  O/P: [2, 4]
