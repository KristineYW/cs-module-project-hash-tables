"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6



"""
If you choose 4 numbers from `q`, call them `a`, `b`, `c`, and `d`:

What are the combinations of `f(a) + f(b)` that are algebraically
equivalent to the combinations of `f(c) - f(d)`?

That is, show all `a`, `b`, `c`, `d` for which this is true:

```
f(a) + f(b) = f(c) - f(d)
```

For the above `q`, we get this sample output:

```
f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
f(1) + f(4) = f(12) - f(4)    10 + 22 = 54 - 22
f(4) + f(1) = f(12) - f(4)    22 + 10 = 54 - 22
f(1) + f(7) = f(12) - f(1)    10 + 34 = 54 - 10
f(4) + f(4) = f(12) - f(1)    22 + 22 = 54 - 10
f(7) + f(1) = f(12) - f(1)    34 + 10 = 54 - 10
f(3) + f(3) = f(12) - f(3)    18 + 18 = 54 - 18
```

The left column shows the `a`-`d` inputs to `f(x)`, and the right column
shows the result from the what `f(x)` returns for each of those.
"""
