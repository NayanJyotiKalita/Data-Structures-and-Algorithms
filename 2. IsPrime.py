IsPrime

Problem Description
Given a number A. Return 1 if A is prime and return 0 if not. 
Note : 
The value of A can cross the range of Integer.

Problem Constraints
1 <= A <= 109

Input Format
The first argument is a single integer A.

Output Format
Return 1 if A is prime else return 0.

Example Input
Input 1:
A = 5
Input 2:
A = 10

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:
5 is a prime number.
Explanation 2:
10 is not a prime number.


CODE:
class Solution:
    # @param A : integer
    # @return an integer
    def isprime(self, A):
        i = 2
        while i * i <= A:
            if A % i == 0:
                return 0
            i += 1
        return int(A >= 2)

'or'

class Solution:
    # @param A : integer
    # @return an integer
    def isprime(self, A):
        ans = True
        for i in range(2, int(A**0.5)+1):
            if A % i == 0:
                ans = False
                break
        if ans == False or A == 1:
            return 0 
        else:
            return 1

'or'

class Solution:
    # @param A : integer
    # @return an integer
    def isprime(self, A):
        if A < 2:
            return 0
        elif A == 2 or A == 3:
            return 1
        else:
            for i in range(2, int(A**0.5)+1):
                if A % i == 0:
                    return 0
        return 1


        
solution = Solution()
