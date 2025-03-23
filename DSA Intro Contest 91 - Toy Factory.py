Toy Factory

Problem Description
In a toy factory, there are N toy blocks arranged in a row. Each toy block has a certain color represented by an integer in the array A of size N. 
The factory manager wants to find the longest contiguous sequence of toy blocks such that all the colors in the sequence are either divisible by 4 or 5. The manager needs your help to determine the length of the longest such sequence.

Problem Constraints
|A| = N
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First argument A, is an array of integers.

Output Format
Return a single integer.

Example Input
Input 1:
A = [4, 1, 10, 15]
Input 2:
A = [1, 9, 2]

Example Output
Output 1:
2
Output 2:
0

Example Explanation
For Input 1:
Consider 0-based indexing:
Subarray [2,3] is the longest subsequence satisfying the conditions.
For Input 2:
There is no subarray which satisfy the conditions.

CODE:

 class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        ans = 0
        for i in range(len(A)):
            if A[i] % 4 == 0 or A[i] % 5 == 0:
                count += 1
            else:
                count = 0
                
            ans = max(ans, count)
        
        return ans


solution = Solution()
print(solution.solve( A = [4, 1, 10, 15] ))
