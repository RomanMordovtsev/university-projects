def multiplyOrder(p):
    n = len(p) - 1
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1])

    return dp[0][n - 1]


test = [10, 100, 5, 50]
print(multiplyOrder(test))
