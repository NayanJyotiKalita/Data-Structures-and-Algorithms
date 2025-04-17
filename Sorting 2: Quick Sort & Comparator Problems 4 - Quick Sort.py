Quick Sort

Problem Description
Given an integer array A, sort the array using Quick Sort.

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
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        self.quicksort(A, 0, len(A) - 1)
        return A 

    def partition(self, A, first, last):

        pivot = A[first]
        left = first + 1
        right = last
        #print("A",A,"p,",pivot,"Al,Ar",A[left],A[right],"l",left,"r",right)
        
        while left <= right:
            #print("loop")
            if A[left] <= pivot:
                left += 1
                #print("left",left)
            elif A[right] > pivot:
                right -= 1
                #print("right",right)
            else:
                A[left], A[right] = A[right], A[left]
                #print("left&right",A)

        A[first], A[left-1] = A[left-1], A[first]
        #print("final",A,left-1,A[left-1],first,last)

        return (left-1)
        
    def quicksort(self, A, start, end):
        if start < end:
            #print("start partition, A, s,e",A,start,end)
            pivotidx=self.partition(A, start, end)
            
            #print("Quicksort1", "A",A,"start",start,"pivotidx",pivotidx-1)
            self.quicksort(A, start, pivotidx-1)
            
            #print("Quicksort2","A",A,"start",pivotidx+1, "end",end)
            self.quicksort(A, pivotidx+1, end)

'or'

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        self.quicksort(A, 0, len(A) - 1)
        return A
    
    def quicksort(self, A, start, end):
        if start >= end:
            return
        pivot = self.partition(A, start, end)
        self.quicksort(A, start, pivot - 1)
        self.quicksort(A, pivot + 1, end)
        
    def partition(self, A, s, e):
        p = A[s]
        i = s + 1

        for j in range(s + 1, e + 1):
            if A[j] <= p:
                A[i], A[j] = A[j], A[i]
                i += 1

        A[s], A[i - 1] = A[i - 1], A[s]

        # for j in range(i, e + 1):
        #     if A[j] == p:
        #         A[i], A[j] = A[j], A[i]
        #         break

        return i - 1


solution = Solution()
print(solution.solve( A = [1, 4, 10, 2, 1, 5] ))  -->  O/P: [1, 1, 2, 4, 5, 10]
