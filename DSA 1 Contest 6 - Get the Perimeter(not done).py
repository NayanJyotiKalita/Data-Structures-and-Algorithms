Get the Perimeter

Problem Description
You are given a row x col grid representing a map where A[i][j] = 1 represents land and A[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. 
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
Please take a look at the examples below for better understanding of the problem.

Problem Constraints
1 <= row, col <= 100
A[i][j] = 0 if the current cell represents water.
A[i][j] = 1 if the current cell represents land.

Input Format
First argument contains a 2D integer array A.

Output Format
Return an integer denoting the perimeter of island.

Example Input
Input 1:
A = [ 
        [0, 1, 0, 0]
        [1, 1, 1, 0]
        [0, 1, 0, 0]
        [1, 1, 0, 0]
    ]
Input 2:
A = [ 
        [1]
    ]

Example Output
Ouput 1:
16
Output 2:
4

Example Explanation
Explanation 1:
The perimeter is the 16 yellow stripes in the image below.
        
Explanation 2:
There is a single cell containing 1. Hence, the perimeter is 4.

CODE:

class Solution:
    
