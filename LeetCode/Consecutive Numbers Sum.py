class Solution:
    def consecutiveNumbersSum(self, n: int):
        self.n = n
        combination = 0
        numbers = list(range(1, self.n+1))
        # print(numbers)
        value = 0
        while value <= self.n+1:
            result = 0
            print(f"\n\nnext iteration {value}")
            for i in range(value, self.n):
                print(f're:{result}')
                result += numbers[i]
                print(f'i:{i} by:{numbers[i]}  re:{result}\n')
                if result == self.n:
                    combination += 1
                    result = 0
                    break
                if result > self.n:
                    break
            value += 1

        return print(combination)


ret = Solution().consecutiveNumbersSum(15)
# 15 = 15, 8 + 7 , 1 + 2 + 3 + 4 + 5

# SOLUTION 1
# # N = (x + 1) + ... + (x + k)
# # N = x k + k(k + 1)/2
# class Solution:
#     def consecutiveNumbersSum(self, N: int) -> int:
#         count = 0
#         # x > 0 --> N/k - (k + 1)/2 > 0
#         upper_limit = ceil((2 * N + 0.25)**0.5 - 0.5) + 1
#         for k in range(1, upper_limit):
#             # x should be integer
#             if (N - k * (k + 1) // 2) % k == 0:
#                 count += 1
#         return count


# SOLUTION 2

# class Solution:
#     def consecutiveNumbersSum(self, N: int) -> int:
#         count = 0
#         upper_limit = ceil((2 * N + 0.25)**0.5 - 0.5) + 1
#         for k in range(1, upper_limit):
#             N -= k
#             if N % k == 0:
#                 count += 1
#         return count
