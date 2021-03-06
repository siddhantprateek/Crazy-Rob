class Solution:
    def maximumWealth(self, accounts: list[list[int]]):
        self.accounts = accounts
        collection_amount = []
        for ac in accounts:
            collection_amount.append(sum(ac))
        return max(collection_amount)


ret = Solution().maximumWealth([[1, 2, 3], [3, 2, 1]])
