def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)
N = int(input("enter a number : "))
print(sum_n(N))
