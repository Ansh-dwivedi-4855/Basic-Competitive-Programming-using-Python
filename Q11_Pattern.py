n = 5

# Top half
for i in range(n, 0, -1):
    print('*' * i + ' ' * (2*(n-i)) + '*' * i)

# Bottom half
for i in range(1, n+1):
    print('*' * i + ' ' * (2*(n-i)) + '*' * i)
