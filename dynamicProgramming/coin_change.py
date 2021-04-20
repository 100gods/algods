def coin(coins, amount):
    n, k, arr = len(coins), amount, coins
    dp = [[0 for i in range(n + 1)] for i in range(k + 1)]
    for i in range(1, k + 1):
        dp[i][0] = -1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            wt = arr[j-1]
            if wt <= i and dp[i - wt][j] != -1:
                left = 1 + dp[i - wt][j]
            else:
                left = -1
            right = dp[i][j - 1]
            if right == -1 or left == -1:
                dp[i][j] = max(left, right)
            else:
                dp[i][j] = min(left, right)
    return dp[k][n]

print(coin([2],3))