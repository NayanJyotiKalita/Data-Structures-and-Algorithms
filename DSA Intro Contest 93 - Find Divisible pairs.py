Find Divisible pairs

Problem Description
Lila and Sam are organizing a mathematical game night. They have two lists of numbers, and they want to count how many pairs of numbers from these lists satisfy a certain divisibility rule. Help them find the total number of such pairs.
You are given 2 integer arrays A and B of lengths N and M respectively.
A pair (i, j) is called good if A[i] is divisible by Bj.
Return the total number of good pairs.

Problem Constraints
1 <= N, M <= 105
1 <= A[i], B[i] <= 105

Input Format
First Argument is an Integer Array A.
Second Argument is an Integer Array B.

Output Format
Return an Integer, denoting the total number of good pairs.

Example Input
Input 1:
A = [1, 3, 4]
B = [1, 3, 4]
Input 2:
A = [1, 2, 4, 12]
B = [2, 4]

Example Output
Output 1:
5
Output 2:
2

Example Explanation
For Input 1:
The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
For Input 2:
The 2 good pairs are (3, 0) and (3, 1).

CODE:

 class Solution:
    # @param A : list of integers
    # @param B : list of integers
     # @return an long
    def totalGoodPairs(self, A, B):
        max_value = 10**5
        countA = [0] * (max_value + 1)
        countB = [0] * (max_value + 1)
        
        for a in A:
            countA[a] += 1
        
        for b in B:
            countB[b] += 1
        
        count = 0
        
        for b in range(1, max_value + 1):
            if countB[b] > 0:
                for c in range(b, max_value + 1, b):
                    count += countB[b] * countA[c]
        
        return count
        
