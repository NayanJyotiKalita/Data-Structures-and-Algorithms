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

'or'

class Solution:
    # Merge two sorted arrays
    def merge(self, sorted, left, mid, right):
        m1 = mid - left + 1
        m2 = right - mid

        arr1 = [0] * m1
        arr2 = [0] * m2

        i = j = 0
        k = left

        while i < m1:
            arr1[i] = sorted[left + i]
            i += 1

        while j < m2:
            arr2[j] = sorted[mid + 1 + j]
            j += 1

        i = j = 0
        while i < m1 and j < m2:
            if arr1[i] <= arr2[j]:
                sorted[k] = arr1[i]
                i += 1
            else:
                sorted[k] = arr2[j]
                j += 1
            k += 1

        while i < m1:
            sorted[k] = arr1[i]
            i += 1
            k += 1

        while j < m2:
            sorted[k] = arr2[j]
            j += 1
            k += 1

    # Merge Sort implementation
    def mergeSort(self, A, L, R):
        if L < R:
            M = (L + R) // 2

            # Divide
            self.mergeSort(A, L, M)
            self.mergeSort(A, M + 1, R)

            # Conquer
            self.merge(A, L, M, R)

    # Sort the subarray specified by indices B and C
    def sortSubarray(self, A, B, C):
        self.mergeSort(A, B, C)
        return A


solution = Solution()
print(solution.sortSubarray( A = [59, 11, 8, 91, 49, 44, 8], B = 4, C = 6 ))  -->  O/P: [59, 11, 8, 91, 8, 44, 49]
