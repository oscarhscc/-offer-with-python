'''
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:

你可以假设：

0 <= n (总金额) <= 1000000
'''

class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n == 0:
            return 0
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        costs = [1, 5, 10, 25]
        for cost in costs:
            for i in range(cost, n + 1):
                dp[i] += dp[i - cost]
        return dp[-1] % 1000000007