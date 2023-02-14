s = int(input())
ls = []
for i in range(s):
  ls.append(int(input()))

def dp(n):
  dp = [0]*(n+3)
  dp[0],dp[1],dp[2] = 1,2,4
  for i in range(3,n+1):
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
  print(dp[n-1])

for l in ls:
  dp(l)