Find All Pair

Problem Description
You are given arrays A, B, and C, each of length N.
Your task is to find the count of all pairs of integers (x, y) such that A[x] is equal to B[C[y]] where 1<= x, y <= N.

Problem Constraints
1 <= |A| =|B| =|C| <= 105
1 <= A[i], B[i], C[i] <= |A|

Input Format
First argument A is an integer.
In the second argument, B is an integer.
In the Third argument, C is an integer.

Output Format
Return an integer.

Example Input
Input 1:
A = [1, 2]
B = [2, 1]
C = [2, 2] 
Input 2:
A = [2, 3, 3]
B = [1, 3, 3]
C = [1, 1, 1] 

Example Output
Output 1:
2
Output 2:
0

Example Explanation
Explanation 1:
valid pairs are (1, 1) and (1, 2)
Explanation 2:
No valid pair

CODE:

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def find_all_pair(self, A, B, C):
        n = len(A)
        
        hm = {}
        for i in range(n):
            j = C[i] - 1
            if 0 <= j < n:
                if B[j] in hm:
                    hm[B[j]] += 1
                else:
                    hm[B[j]] = 1
        
        count = 0
        for i in range(n):
            if A[i] in hm:
                count += hm[A[i]]
            
        return count 


solution = Solution()
print(solution.find_all_pair( A = [1, 2], B = [2, 1], C = [2, 2]  ))  -->  O/P: 2
