
def no_subsets_with_sum(set,sum,n,x):
    if sum == 0:
        return 1
    if n == 0:
        return 0
    if sum%x==0 and set[n-1] <= sum:
        return no_subsets_with_sum(set,sum-set[n-1],n-1,x) + no_subsets_with_sum(set,sum,n-1,x)
    else:
        return no_subsets_with_sum(set, sum, n - 1, x)
if __name__ == "__main__":
    set = [2, 4, 3, 7]
    sum = 6
    n = len(set)
    x = 2
    # t = [[None for i in range(sum+1)] for j in range(n +1)]
    print(no_subsets_with_sum(set,sum,n,x))