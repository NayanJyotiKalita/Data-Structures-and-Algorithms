Print A to 1 function

Problem Description:
You are given an integer A, print A to 1 using using recursion.
Note :- After printing all the numbers from A to 1, print a new line.

Problem Constraints
1 <= A <= 104

Input Format
First argument A is an integer.

Output Format
Print A space-separated integers A to 1.
Note: There should be exactly one space after each integer. Print a new line after printing the A integers

Example Input
Input 1:
10
Input 2:
5

Example Output
Output 1:
10 9 8 7 6 5 4 3 2 1 
Output 2:
5 4 3 2 1 

Example Explanation
Explanation 1:
Print 10 to 1 space separated integers.
Explanation 2:
Print 5 to 1 space separated integers.

CODE:

class Solution:
    # @param A : integer
    def print_Ato1(self, A):
        print(A, end = ' ')
        if A > 1:
            self.solve(A-1)
            return
        print()

'or'

class Solution:
    # @param A : integer
    def print_Ato1(self, A):
        if A == 1:
            print(1, end = " ")
            print()
            return
        else:
            print(A, end = " ")
            self.solve(A-1)

'or'

class Solution:
    # @param A : integer
    def solve(self, A):
        def print_n(n):
            print(n, end = " ")
            if n > 1:
                print_n(n-1)
        print_n(A)
        print()

solution = Solution()
print(solution.print_Ato1( A = 10 )) --> O/P: 10 9 8 7 6 5 4 3 2 1 
