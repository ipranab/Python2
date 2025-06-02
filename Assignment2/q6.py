(a)def example1(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

(b)for i in range(n):
    print(i)

(c)def recursive_function(n):
    if n <= 1:
        return 1
    return recursive_function(n-1) + recursive_function(n-1)

