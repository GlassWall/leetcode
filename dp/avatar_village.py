import sys
n = input()
n = int(n)
arr = input()
arr = arr.split(' ')
for i in range(n):
    arr[i] = int(arr[i])
dp = [-1*sys.maxsize for i in range(n)]
dp[0] = arr[0]

for i in range(1,n):
    for j in range(0,i):
        if arr[i]%arr[j] == 0:
            if dp[j] == -1*sys.maxsize:
                dp[i]=max(dp[i],arr[j])
            else:
                dp[i] = max(dp[i], dp[j])
    if dp[i] != -1*sys.maxsize:
        dp[i] = arr[i] + dp[i]
    else:
        dp[i] = arr[i]

print(dp)