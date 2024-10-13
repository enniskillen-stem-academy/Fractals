def recursive_example(n):
    if n > 0:
        print(n)
        recursive_example(n - 1)

recursive_example(5)