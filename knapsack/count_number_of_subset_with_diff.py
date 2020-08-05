import math
def count_diff(arr, n, diff):
    s1 = (sum(arr) + diff)/2
    t = [[-1 for j in range(int(s1 + 1))] for i in range(n+1)]
    return count_subset_sum(arr, n, s1,t)

def count_subset_sum(arr,n,sum, t):
    if sum == 0:
        return 1
    if n == 0:
        return 0
    if t[n][sum] != -1:
        return t[n][sum]
    if arr[n-1] <= sum:
        t[n][sum] = count_subset_sum(arr, n-1, sum-arr[n-1]) + count_subset_sum(arr, n-1, sum)
    else:
        t[n][sum] = count_subset_sum(arr, n-1, sum)
    return t[n][sum]

if __name__ == "__main__":
    arr = [1, 1, 2, 3]
    n = len(arr)
    diff = 1
    print(count_diff(arr,n,diff))