Tower of Hanoi

Problem Description

In the classic problem of the Towers of Hanoi, you have 3 towers numbered from 1 to 3 (left to right) and A disks numbered from 1 to A (top to bottom) of different sizes which can slide onto any tower.
The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).
You have the following constraints:

Only one disk can be moved at a time.
A disk is slid off the top of one tower onto another tower.
A disk cannot be placed on top of a smaller disk.

You have to find the solution to the Tower of Hanoi problem.
You have to return a 2D array of dimensions M x 3, where M is the minimum number of moves needed to solve the problem.
In each row, there should be 3 integers (disk, start, end), where:

disk - number of the disk being moved
start - number of the tower from which the disk is being moved
end - number of the tower to which the disk is being moved

Problem Constraints
1 <= A <= 18

Input Format
The first argument is the integer A.

Output Format
Return a 2D array with dimensions M x 3 as mentioned above in the description.

Example Input
Input 1:
A = 2
Input 2:
A = 3

Example Output
Output 1:
[1 1 2 ] [2 1 3 ] [1 2 3 ]
Output 2:
[1 1 3 ] [2 1 2 ] [1 3 2 ] [3 1 3 ] [1 2 1 ] [2 2 3 ] [1 1 3 ] 

Example Explanation
Explanation 1:
We shift the first disk to the middle tower.
We shift the second disk to the last tower.
We, finally, shift the first disk from the middle tower to the last tower.
Explanation 2:
We can see that this was the only unique path with minimal moves to move all disks from the first to the third tower.

CODE:

sys.setrecursionlimit(10 ** 6)
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A):
        ans = []
        def rec(disk, start, end):
            l1 = [disk, start, end]
            if disk == 1:
                ans.append(l1)
                return
            # move top (disk - 1) disks from start to buffer, using end as a buffer
            rec(disk - 1, start, 6 - start - end)
            # move top from start to end
            ans.append(l1)
            # move top (disk - 1) disks from buffer to end, using start as a buffer
            rec(disk - 1, 6 - start - end, end)
        rec(A, 1, 3)
        return ans


solution = Solution()
print(solution.towerOfHanoi( A = 3 ))  -->  O/P: [1 1 3 ] [2 1 2 ] [1 3 2 ] [3 1 3 ] [1 2 1 ] [2 2 3 ] [1 1 3 ]
