IsPrime

Problem Description
Given a number A. Return 1 if A is prime and return 0 if not. 
Note : 
The value of A can cross the range of Integer.

Problem Constraints
1 <= A <= 109

CODE:
def solve(self, A):
    i = 2
    while i * i <= A:
        if A % i == 0:
            return 0
        i += 1
    return int(A >= 2)
