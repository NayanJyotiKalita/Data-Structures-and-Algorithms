Find Output

Guess the output for the following program:

def fun(x, n):
    if (n == 0):
        return 1
    elif (n % 2 == 0):
        return fun(x * x, n // 2)
    else:
        return x * fun(x * x, (n - 1) // 2)

  ans = fun(2, 10)
print(ans)

Choose the correct answer from below:

1. 1023

2. 2048

3. 1024

4. None of these

Ans:
3
