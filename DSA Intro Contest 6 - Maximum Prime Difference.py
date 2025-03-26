Maximum Prime Difference

Problem Description
In a kingdom, a mathematician named Arya was given an Array of integers, A of size N. The king challenged her to find the maximum distance between the indices of any two (not necessarily different) prime numbers in the array. If there is no prime number in the given array, return -1.
Help Arya solve this problem to prove her skill.

Problem Constraints
1 <= A.length <= 105
2 <= A[i] <= 100

Input Format
The only argument is an Integer Array, A.

Output Format
Return an Integer, denoting the maximum distance between the indices of any two prime numbers.

Example Input
Input 1:
A = [14, 2, 8, 5, 3]
Input 2:
A = [8, 4, 10, 7, 18]
Input 2:
A = [9, 12, 4]

Example Output
Output 1:
3
Output 2:
0
Input 2:
-1

Example Explanation
For Input 1:
A[1], A[3], and A[4] are prime. 
Choosing A[1] and A[1]  => distance = |1 - 1| = 0
Choosing A[1] and A[3]  => distance = |3 - 1| = 2
Choosing A[1] and A[4]  => distance = |4 - 1| = 3
Choosing A[3] and A[3]  => distance = |3 - 3| = 0
Choosing A[3] and A[4]  => distance = |4 - 3| = 1
Choosing A[4] and A[4]  => distance = |4 - 4| = 0
So the maximum distance is 3.

For Input 2:
There is only 1 prime number at A[3].  
Choosing A[3] and A[3]  => distance = |3 - 3| = 0
So the maximum distance is 3.

For Input 3:
There is no Prime number in the given array.  The answer is -1.

CODE:

 class Solution:
    # @param A : list of integers
    # @return an integer
    def maximumPrimeDifference(self, A):
        c = []
        for i in range(len(A)):
            j = 1
            final = -1
            count = 0
            while j*j <= A[i]:
                if A[i] % j == 0:
                    count += 1
                    if j != A[i] // j:
                        count += 1
                j += 1
            if count == 2:
                c.append(i)
        if len(c) != 0:
            final = max(c) - min(c)
        return final 


solution = Solution()
print(solution.maximumPrimeDifference( A = [8, 4, 10, 7, 18] ))
