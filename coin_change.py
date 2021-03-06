# Classic coin change dp problem.
# Given infinite supply of denominations coin and a target value
# find the minimum number of coins required to acive that target value.


def coin_change(coins, target):
	inf = 10**9	
	dp = [0] + [ inf for i in range(target)]  # target 0 can be acchived using 0 coin and rest are infiniti for now
	for coin in coins:
		for i in range(coin, target+1):
			dp[i] = min(dp[i], dp[i-coin]+1)  # formula for dp
    if dp[target]!=10**9: return dp[target]
	else: return "Impossible"


print(coin_change([],44))  # Impossible
