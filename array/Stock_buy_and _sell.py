def stockBuySell(A, n):
    if A:
        ans = []
        i = 0
        while i < n - 1:
            while i < n - 1 and A[i + 1] <= A[i]:
                i += 1

            if i == n - 1:
                break

            buy = i
            i += 1

            while i < n and A[i] >= A[i - 1]:
                i += 1

            sell = i - 1
            ans.append([buy, sell])
        return ans


print(stockBuySell([100,180,260,310,40,535,695], 7 ))
print(stockBuySell([4,2,2,2,4],5))
print(stockBuySell([11, 42, 49, 96, 23, 20, 49, 26, 26, 18, 73, 2, 53, 59, 34, 99, 25, 2], 18))
print(stockBuySell([57, 69, 12, 59, 5, 9, 29, 29, 99],9))