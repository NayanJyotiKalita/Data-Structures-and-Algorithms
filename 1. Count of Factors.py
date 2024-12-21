Problem Description:

Given an integer A, you need to find the count of it's factors.
Factor of a number is the number which divides it perfectly leaving no remainder.
Example : 1, 2, 3, 6 are factors of 6

Problem Constraints
1 <= A <= 109

CODE:

def solve(self, A):
    count = 0
    i = 1
    while i * i <= A:
        if A % i == 0:
            count += 1
            if A // i != i:
                count += 1
        i += 1
    return count
