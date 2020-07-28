set = [3, 2, 1, 6, 5]
sum = 6
n = 5

t = [[None for i in range(sum+1)] for j in range(n +1)]
for i in range(n+1):
    for j in range(sum+1):
        if j == 0:
            t[i][j] = 1
        if (i == 0) and (j != 0):
            t[i][j] = 0

for i in range(1, n + 1):
    for j in range(1, sum+1):
        if set[i-1] <= j:
            t[i][j] = t[i-1][j - set[i-1]] + t[i-1][j]
        else:
            t[i][j] = t[i-1][j]

print(t[n][sum])