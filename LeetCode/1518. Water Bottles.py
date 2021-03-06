class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int):
        self.numBottles = numBottles
        self.numExchange = numExchange
        
        if self.numBottles > self.numExchange:
            give = self.numBottles // self.numExchange
            drank = self.numBottles + give + 1
            return print(drank)
        elif self.numBottles == self.numExchange:
            give = self.numBottles // self.numExchange
            drank = self.numBottles + give
            return print(drank)
        else:
            return print(self.numBottles)


ret = Solution().numWaterBottles(5, 5)
