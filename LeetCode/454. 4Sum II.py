class Solution:
    def fourSumCount(self, A: list[int], B: list[int], C: list[int], D: list[int]) -> int:
        
        Dict = {}
        ans = 0
        for numa in A:
            for numb in B:
                Dict[numa + numb] = Dict.get(numa + numb, 0) + 1

        for numc in C:
            for numd in D:
                ans += Dict.get(-(numc + numd), 0)

        return print(ans)


ret = Solution().fourSumCount([1,2],[-2,-1],[-1,2],[0,2])