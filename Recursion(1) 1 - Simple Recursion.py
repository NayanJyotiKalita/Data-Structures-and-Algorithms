What will be the output of following program ?

def bar(x, y):
    if y == 0:
        return 0
    return (x + bar(x, y-1))

def foo(x, y):
    if (y == 0):
        return 1
    return bar(x, foo(x, y-1))

print(foo(3, 5))


Choose the correct answer from below:

1. 243

2. 15

3. 18

4. 125

Ans:
1
