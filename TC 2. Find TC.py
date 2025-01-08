'''
What is the time complexity of the following code snippet
'''

def solve(N, M):
  for i in range(1, N + 1):
    if N % i == 0:
      print(i)
  for i in range(1, M + 1):
    if M % i == 0:
      print(i)

Options:
1. O(N)
2. O(M)
3. O(N + M)
3. O(NM)

Ans:
3
