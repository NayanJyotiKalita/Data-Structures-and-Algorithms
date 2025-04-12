Count unique elements

Problem Description
You are given an array A of N integers. Return the count of elements with frequncy 1 in the given array.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First argument A is an array of integers.

Output Format
Return an integer.

Example Input
Input 1:
A = [3, 4, 3, 6, 6]
Input 2:
A = [3, 3, 3, 9, 0, 1, 0]

Example Output
Output 1:
1
Output 2:
2

Example Explanation
Explanation 1:
Only the element 4 has a frequency 1.
Explanation 2:
The elements 9 and 1 has a frequncy 1.

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def count_uniq_ele(self, A):
        
        hm = {}
        for i in range(len(A)):
            if A[i] in hm:
                hm[A[i]] += 1
            else:
                hm[A[i]] = 1

        count = 0
        for i in hm:
            if hm[i] == 1:
                count += 1
        
        return count


solution = Solution()
print(solution.count_uniq_ele( A = [3, 3, 3, 9, 0, 1, 0] ))  -->  O/P: 2
