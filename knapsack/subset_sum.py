def subset_sum(numbers, total, n):
    t = [[None for j in range(total + 1)] for i in range(n+1)]
    # Initialize t array fow when either number of elements to pick = 0 or sum = 0
    for i in range(n+1):
        for j in range(total+1):
            if i == 0:  # if number of elements to make the sum is 0:
                return False
            if j == 0: # if total to find is 0 then:
                return True
    for i in range(1, n+1):
        for j in range(1, total+1):
            if numbers[i-1] <= total:
                t[i][j] = t[i-1][j-numbers[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]


if __name__ == "__main__":
    numbers = [3, 34, 4, 12, 5, 2]
    total = 30
    n = len(numbers)
    print(subset_sum(numbers, total, n))


































    # for i in range(n+1):
    #     for j in range(total+1):
    #         if i == 0:
    #             t[i][j] = False
    #         if j == 0:
    #             t[i][j] = True
    # for i in range(1,n+1):
    #     for j in range(1, total+1):
    #         if numbers[i-1] <= j:
    #             t[i][j] = t[i-1][j-numbers[i-1]] or t[i-1][j]
    #         else:
    #             t[i][j] = t[i-1][j]
    # return t[n][total]