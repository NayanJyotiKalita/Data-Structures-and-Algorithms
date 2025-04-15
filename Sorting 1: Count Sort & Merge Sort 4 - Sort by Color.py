Sort by Color

Problem Description
Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will represent the colors as,
red -> 0
white -> 1
blue -> 2
Note: Using the library sort function is not allowed.

Problem Constraints
1 <= N <= 1000000
0 <= A[i] <= 2

Input Format
First and only argument of input contains an integer array A.

Output Format
Return an integer array in asked order

Example Input
Input 1 :
    A = [0, 1, 2, 0, 1, 2]
Input 2:
    A = [0]

Example Output
Output 1:
    [0, 0, 1, 1, 2, 2]
Output 2:
    [0]

Example Explanation
Explanation 1:
    [0, 0, 1, 1, 2, 2] is the required order.
Explanation 2:
    [0] is the required order

CODE:

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        freq = [0] * 3  # since the max value of the element in A is 2 therefore it lenght should be (max + 1)

        for i in range(len(A)):
            freq[A[i]] += 1            # Adding element value to freq list in which the element is equal to indices of freq

        j = 0
        for i in range(len(freq)): # this will cover all the elements in the freq list
            for k in range(freq[i]): # this loop will run the times of value of the count of element in freq list
                A[j] = i
                j += 1
        return A


solution = Solution()
print(solution.sortColors( A = [0, 1, 2, 0, 1, 2] ))  -->  O/P: [0, 0, 1, 1, 2, 2]
