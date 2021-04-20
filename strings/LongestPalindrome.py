def longest_plaindrome(s: str) -> str :
    if s:
        n, res = len(s), ""
        if n == 1:
            return s
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
            res = res if res else s[i]
            if i+1 < n and s[i] == s[i+1] :
                print(res)
                dp[i][i+1] = 1
                res = s[i:i+2]
                print(res,s[i:i+2])

        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                print(i, j,dp[i+1][j-1],(i+1,j-1),(s[i],s[j]))
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    res = res if len(res) > len(s[i:j+1]) else s[i:j+1]
                    print(res)
        for p in dp:
            print(p)
        return res

print(longest_plaindrome("abb"))

