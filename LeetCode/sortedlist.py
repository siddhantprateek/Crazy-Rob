class Solution:
    def mergeKLists(self, lists: list[list]):

        self.lists = lists
        new_lists = []

        for char in range(len(self.lists)):
            new_lists += self.lists[char]

        sortedlists = sorted(new_lists)

        print(sortedlists)


ret = Solution().mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]])
