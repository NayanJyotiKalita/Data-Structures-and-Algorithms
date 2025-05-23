Print Array using Recursion

Problem Description
You are given an array A. Print the elements of the array using recursion.
NOTE :
You are required to not use any loops, You can create new functions.
Don't change the signature of the function PrintArray.
Print a new empty line after printing the output.

Problem Constraints
1 <= | A | <= 100
-1000 <= A[i] <= 1000

Input Format
One line containing the array A

Output Format
Print the elements of the array in the sequential order.

Example Input
Input 1 :
A = [6, -2, 5, 3]
Input 2 :
A = [1]

Example Output
Output 1 :
6 -2 5 3 
Output 2 :
1 

Example Explanation
Print the elements in their order.

CODE:

class Solution:
    # @param A : list of integers
    def printA(self, A, idx):
        if idx == len(A):
            return
        print(A[idx], end = ' ')
        self.printA(A, idx+1)

    def PrintArray(self, A):
        self.printA(A, 0)
        print()

'or'

class Solution:
    # @param A : list of integers
    def PrintArray(self, A):
        def array(A, idx):
            if idx == len(A):
                return
            print(A[idx], end = " ")
            array(A, idx+1)

        array(A, 0)
        print()


solution = Solution()
print(solution.PrintArray( A = [6, -2, 5, 3] ))  -->  O/P: 6 -2 5 3 
