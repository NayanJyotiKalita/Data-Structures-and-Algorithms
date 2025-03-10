John and Maths

Problem Description
John is a math enthusiast who loves to explore number patterns. One day, he came across an interesting problem: given an array A of size N with distinct elements, he wanted to know how many elements in the array were divisible by 7 and had at least 2 strictly greater elements.
Can you help John solve the problem?

Problem Constraints
1 <= A.length <= 105
1 <= A[i] <= 109

Input Format
The only argument is the array A.

Output Format
Return an Integer.

Example Input
Input 1:
A = [8, 7, 11, 9, 14]
Input 2:
A = [14, 7, 21, 45, 23]

Example Output
Output 1:
1
Output 2:
3

Example Explanation
Explanation 1:
In the array [8, 7, 11, 9, 14], 7 is the only element at position 1 which is divisible by 7 and has at least 2 elements strictly greater to it.
14 is also divisible by 7 but it has no element greater than itself.

CODE:

 class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse = True)
        count = 0
        for i in range(len(A)):
            if A[i] % 7 == 0 and i >= 2:
                count += 1
        return count 
