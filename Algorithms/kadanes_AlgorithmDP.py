#https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

import math
# Kadane's Algorithm
def MaximumSubarray(nums: list[int]):
    # in this algorithm we mantain a local maximum

    local_max = 0
    global_max = -math.inf
    for current in nums:
        local_max = max(current, current + local_max)# we will maintain prev local_max with current

        # if local_max > global_max:
        #     global_max = local_max
        # or
        global_max = max(global_max, local_max)

    return global_max

print(MaximumSubarray([-2,1,-3,4,-1,2,1,-5,4]))
