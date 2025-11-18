def print_reverse(n):
    if n == 0:
        return
    print(n, end=" ")
    print_reverse(n - 1)
N = int(input("enter a number : "))

print_reverse(N)
