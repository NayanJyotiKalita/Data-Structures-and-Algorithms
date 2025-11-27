# Decimal to Binary

Problem Description
You are given an integer A in decimal (base 10).
Return a string denoting the binary (base 2) form of the integer A.

Problem Constraints
1 <= A <= 109

Input Format
The first line of input contains the integer T, denoting the number of test cases.
Next T lines contain a single integer A, denoting the integer for that test case.

Output Format
Print T lines. In each line, print the string denoting the binary representation of A.

Example Input
Input 1:
 1
 10
Input 2:
 2
 10
 11

Example Output
Output 1:
 1010
Output 2:
 1010
 1011

Example Explanation
Explanation 1:
The binary form of 10 is given by -> '1010'
Explanation 2:
The binary form of 11 is given by -> '1011'

CODE:

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    for i in range(T):
        A = int(input())
        rem = 0
        ans = ''
        while A > 0:
            rem = A % 2
            ans = str(rem) + ans
            A = A // 2
        print(ans)

if __name__ == '__main__':
    main()
