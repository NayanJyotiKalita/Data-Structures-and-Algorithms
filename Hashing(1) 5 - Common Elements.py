Common Elements

Problem Description
Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.
NOTE:
Each element in the result should appear as many times as it appears in both arrays.
The result can be in any order.

Problem Constraints
1 <= N, M <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A of size N.
Second argument is an integer array B of size M.

Output Format
Return an integer array denoting the common elements.

Example Input
Input 1:
 A = [1, 2, 2, 1]
 B = [2, 3, 1, 2]
Input 2:
 A = [2, 1, 4, 10]
 B = [3, 6, 2, 10, 10]

Example Output
Output 1:
 [1, 2, 2]
Output 2:
 [2, 10]

Example Explanation
Explanation 1:
 Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
Explantion 2:
 Elements (2, 10) appears in both the array.

CODE:

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def common_ele(self, A, B):
        hm_A = {}
        hm_B = {}

        for i in A:
            if i in hm_A:
                hm_A[i] +=1
            else:
                hm_A[i] = 1
        
        for i in B:
            if i in hm_B:
                hm_B[i] += 1
            else:
                hm_B[i] = 1
        
        result = []
        for i in hm_A:
            if i in hm_B:
                result.extend([i] * min(hm_A[i], hm_B[i]))
        
        return result

'or'

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        hm_A = {}
        hm_B = {}

        for i in A:
            if i in hm_A:
                hm_A[i] +=1
            else:
                hm_A[i] = 1
        
        for i in B:
            if i in hm_B:
                hm_B[i] += 1
            else:
                hm_B[i] = 1

        result = []
        for i in hm_A:
            if i in hm_B:
                count = min(hm_A[i], hm_B[i])
                while count > 0:
                    result.append(i)
                    count -= 1
                    
        return result


solution = Solution()
print(solution.common_ele( A = [1, 2, 2, 1], B = [2, 3, 1, 2] ))  -->  O/P: [1, 2, 2]
