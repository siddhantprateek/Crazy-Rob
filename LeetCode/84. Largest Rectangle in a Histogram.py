class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
            stack = []
            maximum = 0
            stack.append(0)

            for i in range(1, len(heights)):
                while len(stack) != 0 and heights[i] < heights[stack[-1]]:
                    maximum = self.getMax(heights, stack, maximum, i)
                stack.append(i)

            i = len(heights)
            while len(stack) != 0:
                maximum = self.getMax(heights, stack, maximum, i)


            return print(maximum)


    def getMax(self, heights, stack, maximum, i):

            area = 0
            popped = stack.pop()
            if len(stack) == 0:
                area = heights[popped]*i
            else:
                area = heights[popped]*(i - stack[-1] - 1)

            return max(area, maximum)

sol = Solution().largestRectangleArea([2,1,5,6,2,3])