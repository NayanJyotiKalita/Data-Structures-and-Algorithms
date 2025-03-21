Q. Count of primes

Problem Description
You will be given an integer n. You need to return the count of prime numbers less than or equal to n.

Problem Constraints
0 <= n <= 10^3

Input Format
Single input parameter n in function.

Output Format
Return the count of prime numbers less than or equal to n.

Example Input
Input 1:
19
Input 2:
1

Example Output
Output 1:
8
Output 2:
0

Example Explanation
Explanation 1:
Primes <= 19 are 2, 3, 5, 7, 11, 13, 17, 19
Explanation 2:
There are no primes <= 1


CODE

def count_of_prime(self, A):
    def isprime(x):
        factors = 0
        for i in range(1, x+1):
            if x % i == 0:
                factors += 1
        if factors == 2:
            return True
        else:
            return False

    count = 0
    for i in range(2, A+1):
        if isprime(i) == True:
            count += 1
    return count

solution = Solution()
print(solution.count_of_prime(A = 19))
