import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
dp = [0] * 300
dp[0] = nums[0]

if n > 1:
    dp[1] = nums[0] + nums[1]

if n > 2:
    dp[2] = max(nums[0] + nums[2], nums[1] + nums[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + nums[i-1] + nums[i], dp[i-2] + nums[i])

print(dp[n-1])