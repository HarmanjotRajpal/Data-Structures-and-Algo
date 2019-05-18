amount = 11
coins = [1,2,5]
dp = []

for i in range(0, amount+1):
    dp.append(amount+1)
dp[0]= 0   
for i in range(1, len(dp)):
    for coin in coins:
        dp[i] = min(dp[i-coin]+1, dp[i])
print(dp)
res = dp[-1]
print(res)
           
