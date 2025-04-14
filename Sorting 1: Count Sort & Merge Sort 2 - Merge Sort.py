Merge Sort

Problem Description
Given an integer array A, sort the array using Merge Sort.

Problem Constraints
1 <= |A| <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A.

Output Format
Return the sorted array.

Example Input
Input 1:-
A = [1, 4, 10, 2, 1, 5]
Input 2:-
A = [3, 7, 1]

Example Output
Output 1:-
[1, 1, 2, 4, 5, 10]
Output 2:-
[1, 3, 7]

Example Explanation
Explanation 1 and 2:
Return the sorted array.

CODE:

class Solution:
    def solve(self, A):
        return self.merge_sort(A)
    
    def merge_sort(self, A):
        if len(A) <= 1:
            return A

        mid = len(A) // 2
        left = self.merge_sort(A[ : mid])
        right = self.merge_sort(A[mid : ])
        
        return self.merge_sorted_array(left, right)
    
    def merge_sorted_array(self, A, B):
        i, j = 0, 0
        ans = []

        while i < len(A) or j < len(B):
            if A[i] <= B[j]:
                ans.append(A[i])
                i += 1
            else:
                ans.append(B[j])
                j += 1

        while i < len(A):
            ans.append(A[i])
            i += 1
        while j < len(B):
            ans.append(B[j])
            j += 1

        return ans


solution = Solution()
print(solution.solve( A = [1, 4, 10, 2, 1, 5] ))  -->  O/P: [1, 1, 2, 4, 5, 10]
