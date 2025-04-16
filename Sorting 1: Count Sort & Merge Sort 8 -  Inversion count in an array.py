Inversion count in an array

Problem Description
Given an array of integers A. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).

Problem Constraints
1 <= length of the array <= 105
1 <= A[i] <= 109

Input Format
The only argument given is the integer array A.

Output Format
Return the number of inversions of A modulo (109 + 7).

Example Input
Input 1:
A = [1, 3, 2]
Input 2:
A = [3, 4, 1, 2]

Example Output
Output 1:
1
Output 2:
4

Example Explanation
Explanation 1:
The pair (1, 2) is an inversion as 1 < 2 and A[1] > A[2]
Explanation 2:
The pair (0, 2) is an inversion as 0 < 2 and A[0] > A[2]
The pair (0, 3) is an inversion as 0 < 3 and A[0] > A[3]
The pair (1, 2) is an inversion as 1 < 2 and A[1] > A[2]
The pair (1, 3) is an inversion as 1 < 3 and A[1] > A[3]

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def inversion_count(self, A):
        self.count=0
        self.mergesort(A)
        return self.count%((10**9)+7)

    def mergesorted_Array(self,A,B):
        i=0
        j=0
        ans=[]
        while i<len(A) and j<len(B):
            if A[i]<=B[j]:
                ans.append(A[i])
                i+=1
            else:
                ans.append(B[j])
                j+=1
                self.count+=(len(A)-i)
        while i<len(A):
            ans.append(A[i])
            i+=1
        while j<len(B):
            ans.append(B[j])
            j+=1
        return ans


    def mergesort(self,A):
        if len(A)<=1:
            return A 
        mid=len(A)//2
        left=self.mergesort(A[:mid])
        right=self.mergesort(A[mid:])
        return self.mergesorted_Array(left,right)


solution = Solution()
print(solution.inversion_count( A = [3, 4, 1, 2] ))  -->  O/P: A = [3, 4, 1, 2]
