class Solution:
    def addTwoNumbers(self, l1: list, l2: list):
        l1_size = len(l1) -1
        l2_size = len(l2) -1
        num_l1, num_l2 = 0, 0
        for i in range(l1_size+ 1):
            num_l1 += (l1[l1_size])*(10**(l1_size))
            l1_size -= 1
        print(num_l1)
        for i in range(l2_size+1):
            num_l2 += (l2[l2_size])*(10**(l2_size))
            l2_size -= 1
        print(num_l2)
        add = num_l1 + num_l2
        print(add)
        results = []
        for i in str(add):
            results.append(int(i))
        print(results)

ret = Solution().addTwoNumbers([2,4,3], [5,6,4])
