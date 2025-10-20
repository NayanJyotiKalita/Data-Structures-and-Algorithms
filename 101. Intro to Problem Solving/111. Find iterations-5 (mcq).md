# Find Number of Iterations - 5

## Q. Find the total number of iterations in the following code:

```java
void solve(int N, int M)
{
    int count = 0;
    for (int i = 1; i <= N; i++)
    {
        if (N % i == 0)
            count++;
    }
    for (int i = 1; i <= M; i++)
    {

        if (M % i == 0)
            count++;
    }
    print count;
}
```

---

## Choose the correct answer from below:

    1. N

    2. N + M

    3. M

    4. N/2 + M/2

---

## Answer
*2*
