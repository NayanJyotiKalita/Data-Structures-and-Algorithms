Sort subarray with left and right index

Problem Constraints
1 ≤ N ≤ 105
0 ≤ A[i] ≤ 109
0 ≤ B ≤ C ≤ N - 1

Input Format
First argument is the array A of length N. The next two arguments are the integers B and C.

Output Format
Return the array after sorting the [B, C] subarray.

Example Input
Input:
A = [59, 11, 8, 91, 49, 44, 8]
B = 4
C = 6
Input 2:
A = [50, 40, 30, 20, 10]
B = 0
C = 3

Example Output
Output:
[59, 11, 8, 91, 8, 44, 49]
Output:
[20, 30, 40, 50, 10]

Example Explanation
Explanation 1:
Initially the subarray [B, C], i.e. A[4, 6] = [49, 44, 8].
After sorting this becomes [8, 44, 49].
It can be seen that this subarray gets sorted and rest of the array remains unchanged!

Explanation 2:
Initially the subarray [B, C], i.e. A[0, 3] = [50, 40, 30, 20].
After sorting this becomes [20, 30, 40, 50].
It can be seen that this subarray gets sorted and rest of the array remains unchanged!

CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def sortSubarray(self, A, B, C):
        temp = A[B:C+1]
        temp.sort()
        A[B:C+1] = temp
        return A
