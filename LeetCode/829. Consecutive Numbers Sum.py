class Solution:
    def consecutiveNumbersSum(self, n: int):
        self.n = n

        combination = 0
        result = 0
        # """
        # #size = self.n
        # # for i in range(size+1):
        # #     j = i + 1
        # #     print("\n")
        # #     print(f'i:{i} , j:{j} ')
        # #     result = 0
        # #     for j in range(i+1, size+1):
        # #         result += i + j
        # #         print(f'{i} , {j} r: {result}')
        # #         if result == self.n:
        # #             combination += 1
        # #             result = 0
        # #         else:
        # #             result = 0
        # # return print(combination)
        # """
        numbers = list(range(1, self.n+1))
        print(numbers)
        value = 0
        while value <= self.n+1:
            result = 0
            print("next iteration")
            for i in range(value, self.n+1):
                print(f'\nre:{result}')
                result += numbers[i]
                print(f'i:{i} re:{result}\n')
                if result == self.n:
                    combination += 1
                    result = 0
            value += 1
            print(f'v:{value}')
        return print(combination)


ret = Solution().consecutiveNumbersSum(15)
