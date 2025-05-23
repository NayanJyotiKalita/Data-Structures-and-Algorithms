Noble Integer

Problem Description
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.

Problem Constraints
1 <= |A| <= 2*105
-108 <= A[i] <= 108

Input Format
First and only argument is an integer array A.

Output Format
Return 1 if any such integer p is present else, return -1.

Example Input
Input 1:
 A = [3, 2, 1, 3]
Input 2:
 A = [1, 1, 3, 3]

Example Output
Output 1:
 1
Output 2:
 -1

CODE:

   class Solution:
	# @param A : list of integers
	# @return an integer
	def noble_int(self, A):
	A.sort(reverse = True)
	count = -1
	count_sum = 0
	if A[0] == 0:
	    return 1
	for i in range(1, len(A)):
	    if A[i] != A[i-1]:
		count_sum = i
	    if count_sum == A[i]:
		count += 1
		if count == 0:
		    return 1
	return count

'or'

   class Solution:
	# @param A : list of integers
	# @return an integer
	def noble_int(self, A):
	A.sort(reverse = True)
	count = 0
        if A[0] == 0:
            return 1
        for i in range(1, len(A)):
            if A[i] != A[i-1]:
                count = i
            if A[i] == count:
                return 1
        return -1

'or'

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        inputSize = len(A)
        A.sort()
        start = A[0]
        for i in range(inputSize):
            if (start != A[i]) and (start == (inputSize - i)):
                return 1
            start = A[i]
        if start == 0:
            return 1
        return -1


solution = Solution()
print(solution.noble_int(A = [3, 2, 1, 3]))  -->  O/P: 1
