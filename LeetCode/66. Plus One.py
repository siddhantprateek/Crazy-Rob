class Solution:
    def plusOne(self, digits: list[int]):
        digits_size = len(digits) -1
        num = 0
        for i in range(digits_size+1):
            num += (digits[i])*(10**(digits_size))
            digits_size -= 1
        return_num = []
        num +=1
        for i in str(num):
            return_num.append(int(i))
        return print(return_num)

ret = Solution().plusOne([0,0])