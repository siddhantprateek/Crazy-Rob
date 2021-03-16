class Solution:
    def generateParenthesis(self, size: int, result = [], proc = "") -> List[str]:



        if len(proc) == size:
            result.append(proc)
            return

        item = bracket[]
        generateParenthesis(size, result, proc + item)    

        Generate = []
        brackets = ["(", ")"]

        for item in brackets:
            