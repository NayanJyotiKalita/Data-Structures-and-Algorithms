Subarray with given sum and length

Problem Description
Given an array A of length N. Also given are integers B and C.
Return 1 if there exists a subarray with length B having sum C and 0 otherwise

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 104
1 <= B <= N
1 <= C <= 109

Input Format
First argument A is an array of integers.
The remaining arguments B and C are integers

Output Format
Return 1 if such a subarray exist and 0 otherwise

Example Input
Input 1:
A = [4, 3, 2, 6, 1]
B = 3
C = 11
Input 2:
A = [4, 2, 2, 5, 1]
B = 4
C = 6

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:
The subarray [3, 2, 6] is of length 3 and sum 11.
Explanation 2:
There are no such subarray.

CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def subarray_sum_length(self, A, B, C):
        ans = 0
        summ = 0

        for i in range(B):
            summ += A[i]
        if summ == C:
            return 1
        
        i, j = 1, B
        while j < len(A):
            summ += A[j] - A[i - 1]
            if summ == C:
                return 1
            i += 1
            j += 1
        return 0

'or'

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def subarray_sum_length(self, A, B, C):
        sum = 0
    	for i in range(len(A)):
    		sum += A[i]
    		if(i >= B):
    		    sum -= A[i - B]
    		if(sum == C and i >= B - 1):
    		    return 1
    	return 0


solution = Solution()
print(solution.subarray_sum_length(A = [4, 3, 2, 6, 1], B = 3, C = 11))
