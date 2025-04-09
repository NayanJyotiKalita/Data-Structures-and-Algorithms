Largest Coprime Divisor

Problem Description
You are given two positive numbers A and B . You need to find the maximum valued integer X such that:
X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1

Problem Constraints
1 <= A, B <= 109

Input Format
First argument is an integer A.
Second argument is an integer B.

Output Format
Return an integer maximum value of X as descibed above.

Example Input
Input 1:
 A = 30
 B = 12
Input 2:
 A = 5
 B = 10

Example Outpu
Output 1:
 5
Output 2:
 1

Example Explanation
Explanation 1:
 All divisors of A are (1, 2, 3, 5, 6, 10, 15, 30). 
 The maximum value is 5 such that A%5 == 0 and gcd(5,12) = 1
Explanation 2:
 1 is the only value such that A%5 == 0 and gcd(1,10) = 1

CODE:

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def cpFact(self, A, B):
        # based on a mathematic concept, check notes for more info
        x = A
        # if self.gcd(x, B) == 1:
        #     return A

        while self.gcd(x, B) > 1:
            x = x // self.gcd(x, B)
        return x

    def gcd(self, x, B):
        if B == 0:
            return x
        return self.gcd(B, x % B)


solution = Solution()
print(solution.cpFact( A = 30, B = 12 ))  -->  O/P: 5
