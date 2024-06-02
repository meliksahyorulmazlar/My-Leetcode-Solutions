class Solution(object):
    def maximumWealth(self, accounts):
        greatest = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > greatest:
                greatest = wealth
        return greatest