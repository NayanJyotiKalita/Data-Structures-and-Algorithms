Closest MinMax

Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
and at least one occurrence of the minimum value of the array.

Problem Constraints
1 <= |A| <= 2000

Input Format
First and only argument is vector A

Output Format
Reurn the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array

Example Input
Input 1:
A = [1, 3, 2]
Input 2:
A = [2, 6, 1, 6, 9]
  
Example Output
Output 1:
 2
Output 2:
 3

Example Explanation
Explanation 1:
 Take the 1st and 2nd elements as they are the minimum and maximum elements respectievly.
Explanation 2:
 Take the last 3 elements of the array.

CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def closest_minmax(self, A):

        n = len(A)
        maxi = max(A)
        mini = min(A)
        last_max = -1
        last_min = -1
        ans = n

        if mini == maxi:
            return 1

        for i in range(n):
            if A[i] == maxi:
                last_max = i
                if last_min != -1:
                    ans = min(ans, last_max - last_min + 1)
            
            elif A[i] == mini:
                last_min = i
                if last_max != -1:
                    ans = min(ans, last_min - last_max + 1)
        
        return ans

'or'
'This is a more elaborative code in terms of finding out the max and min'

class Solution:
    # @param A : list of integers
    # @return an integer
    def closest_minmax(self, A):

        ans = len(A)
        length = len(A)
        last_min = -1
        last_max = -1

        maxi = A[0]
        for i in range(len(A)):
            if A[i] > maxi:
                maxi = A[i]

        mini = A[0]
        for i in range(len(A)):
            if A[i] < mini:
                mini = A[i]
              
        if maxi == mini:
            return 1
        else:
            for i in range(len(A)):
                if A[i] == mini:
                    last_min = i
                    if last_max != -1:
                        length = last_min - last_max + 1
                        ans = min(ans, length)        
                elif A[i] == maxi:
                    last_max = i
                    if last_min != -1:
                        length = last_max - last_min + 1
                        ans = min(ans, length)

        return ans

solution = Solution()
print(solution.closest_minmax( A = [2, 6, 1, 6, 9] ))  -->  O/P: 3
