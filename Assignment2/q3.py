def generate_increasing(n, start=1, prefix=""):
    if n == 0:
        print(prefix)
        return
    for i in range(start, 10):
        generate_increasing(n - 1, i + 1, prefix + str(i))

generate_increasing(2)
