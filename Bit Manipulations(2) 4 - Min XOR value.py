Min XOR value

Problem Description
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Problem Constraints
2 <= length of the array <= 100000
0 <= A[i] <= 109

Input Format
First and only argument of input contains an integer array A.

Output Format
Return a single integer denoting minimum xor value.

Example Input
Input 1:
 A = [0, 2, 5, 7]
Input 2:
 A = [0, 4, 7, 9]

Example Output
Output 1:
 2
Output 2:
 3

Example Explanation
Explanation 1:
 0 xor 2 = 2

CODE:

class Solution:
	# @param A : list of integers
	# @return an integer
	def findMinXor(self, A):
		ans=2**31-1
		A.sort()
		'''
		we sort and difference between two adjecent close values always lead to min XOR value
		For instance, what would be the result of XORing 5 and 6, compared to XORing 5 and 100?
		'''
		for i in range(1,len(A)):
			ans=min(ans,A[i-1]^A[i])
        return ans


solution = Solution()
print(solution.findMinXor( A = [0, 2, 5, 7] ))  -->  O/P: 2
