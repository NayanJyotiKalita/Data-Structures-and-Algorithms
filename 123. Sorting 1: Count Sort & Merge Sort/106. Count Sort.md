Count Sort

Problem Description
Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.

Problem Constraints
1 <= |A| <= 105
1 <= A[i] <= 105

Input Format
The first argument is an integer array A.

Output Format
Return an integer array that is the sorted array A.

Example Input
Input 1:
A = [1, 3, 1]
Input 2:
A = [4, 2, 1, 3]

Example Output
Output 1:
[1, 1, 3]
Output 2:
[1, 2, 3, 4]

Example Explanation
For Input 1:
The array in sorted order is [1, 1, 3].
For Input 2:
The array in sorted order is [1, 2, 3, 4].

CODE:

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def count_sort(self, A):
        freq = [0] * (max(A) + 1)

        for i in range(len(A)):
            freq[A[i]] += 1

        idx = 0
        for i in range(len(freq)):
            count = freq[i]
            for j in range(count):
                A[idx] = i
                idx += 1
        
        return A


solution = Solution()
print(solution.count_sort( A = [1, 3, 2, 1] ))  -->  O/P: [1, 1, 2, 3]
