Majority Element (One Third) - N/3 Repeat Number

Problem Description
You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.
If there are multiple solutions, return any one.
Note: Read-only array means that the input array should not be modified in the process of solving the problem

Problem Constraints
1 <= N <= 7*105
1 <= A[i] <= 109

Input Format
The only argument is an integer array A.

Output Format
Return an integer.

Example Input
Input 1:
[1 2 3 1 1]
Input 2:
[1 2 3]

Example Output
Output 1:
1
Output 2:
-1

Example Explanation
Explanation 1:
1 occurs 3 times which is more than 5/3 times.
Explanation 2:
No element occurs more than 3 / 3 = 1 times in the array.

CODE:

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majority_element_ome_third(self, A):
        n = len(A)

        if n==0:
            return -1

        if n==1:
            return A[0]

        first = -1
        second = -1
        count1 = 0
        count2 = 0
        for i in range(n):
            if A[i] == first:
                count1 += 1

            elif A[i] == second:
                count2+=1
                
            elif count1 == 0:
                first = A[i]
                count1 = 1

            elif count2 == 0:
                second = A[i]
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        #print("c1,c2", co
        elementcount1 = 0
        elementcount2 = 0
        for i in range(len(A)):
            if A[i]==first:
                elementcount1+=1
            elif A[i]==second:
                elementcount2+=1
        #print("ec1,ec2", elementcount1, elementcount2)
        

        if elementcount1 > n//3:
            return first
        elif elementcount2 > n//3:
            return second
            
        return -1

solution = Solution()
print(solution.majority_element_ome_third(A = [1, 2, 3, 1, 1]))
