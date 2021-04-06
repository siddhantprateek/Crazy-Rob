def combinationSum2(candidates: list[int], target: int, result=[] , proc=[]):
        
    if sum(proc) == target:
        result.append(proc)
        return
    
    if sum(proc) < target or sum(proc) > target:
        item = candidates[0]
        combinationSum2(candidates[1:], target, result, proc + [item])
        combinationSum2(candidates[1:], target, result, proc)

    return print(proc)

combinationSum2([10,1,2,7,6,1,5], 8)