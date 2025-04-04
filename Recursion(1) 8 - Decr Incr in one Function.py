Decreasing Increasing in one Function

Problem Description
Print N numbers in Decreasing Order and then in Increasing Order.
You are given a positive number N.
You are required to print the numbers from N to 1.
You are required to not use any loops. Don't change the signature of the function DecThenInc function.
Note : Please print an new line after printing the output.

Problem Constraints
1 <= N <= 100

Input Format
The first line contains a single integer N.

Output Format
A single line having number printed from N to 1 and then from 1 to N.

Example Input
Input 2:
1
Input 1:
4

Example Output
Output 1:
1 1
Output 2:
4 3 2 1 1 2 3 4

CODE:

class Solution:
    # @param A : integer
    def DecThenInc(self, A):
        self.dec(A)
        self.inc(A)
        print()
        
    def inc(self, n):
        if n == 1:
            print(1, end = ' ')
            return
        self.inc(n-1)
        print(n, end = " ")

    def dec(self, n):
        print(n, end = " ")
        if n > 1:
            self.dec(n-1)
            return


solution = Solution()
print(solution.DecThenInc( A = 4 )) --> O/P: 4 3 2 1 1 2 3 4
