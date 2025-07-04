Minimum Swaps

Problem Description
Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.
Note: It is possible to swap any two elements, not necessarily consecutive.

Problem Constraints
1 <= length of the array <= 100000
-109 <= A[i], B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the minimum number of swaps.

Example Input
Input 1:
 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8
Input 2:
 A = [5, 17, 100, 11]
 B = 20

Example Output
Output 1:
 2
Output 2:
 1

Example Explanation
Explanation 1:
 A = [1, 12, 10, 3, 14, 10, 5]
 After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
 After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
 Now, all elements less than or equal to 8 are together.
Explanation 2:
 A = [5, 17, 100, 11]
 After swapping 100 and 11, A => [5, 17, 11, 100].
 Now, all elements less than or equal to 20 are together.

CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def minimum_swaps(self, A, B):
        gratervalues = 0
        lesservalues = 0
        #check number of lesser elements than B in the array 
        for i in range(len(A)):
            if A[i] <= B:
                lesservalues += 1
        # print(lesservalues)

        #check number of greater elements than B in the range of lesservalues 
        for i in range(lesservalues):
            if A[i] > B:
                gratervalues += 1
        ans = gratervalues

        # print("ans",gratervalues)

        #Sliding window technique between lesser range and n
        #check if the current element is greater than B increase the count
        #check if the previous array (i-lesservalues)  is greater than B decrease the count
        for i in range(lesservalues,len(A)):
            
            if A[i] > B:
                # print("i, A[i]", i, A[i])
                gratervalues += 1

            if A[i-lesservalues] > B:
                # print("i, A[i-lesservalues]", i, A[i-lesservalues])
                gratervalues -= 1

            # print("gt", gratervalues)

            ans = min(ans, gratervalues)

        return ans


solution = Solution()
print(solution.minimum_swaps( A = [1, 12, 10, 3, 14, 10, 5], B = 8 ))  -->  O/P: 2
