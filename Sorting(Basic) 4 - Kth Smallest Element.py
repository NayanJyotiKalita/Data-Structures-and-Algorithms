Kth Smallest Element

Problem Description
Find the Bth smallest element in given array A .
NOTE: Users should try to solve it in less than equal to B swaps.

Problem Constraints
1 <= |A| <= 100000
1 <= B <= min(|A|, 500)
1 <= A[i] <= 109

Input Format
The first argument is an integer array A.
The second argument is integer B.

Output Format
Return the Bth smallest element in given array.

Example Input
Input 1:
A = [2, 1, 4, 3, 2]
B = 3
Input 2:
A = [1, 2]
B = 2

Example Output
Output 1:
 2
Output 2:
 2

Example Explanation
Explanation 1:
 3rd element after sorting is 2.
Explanation 2:
 2nd element after sorting is 2.

CODE:

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
	        a = list(A)
	        for i in range(B):
	            mini = i
	            for j in range(i + 1, len(a)):
	                if a[j] < a[mini]:
	                    mini = j
	            a[i], a[mini] = a[mini], a[i]
	        return a[B-1]

'or'

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
		A = list(A)
	        A.sort()
	        return A[B-1]


solution = Solution ()
print(solution.kthsmallest(A = [2, 1, 4, 3, 2], B = 3))  -->  O/P: 2
