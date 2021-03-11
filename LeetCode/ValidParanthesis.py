class Solution:
    def isValid(self, string: str) -> bool:

        stack = []
        bracket_map = {"[": "]", "(": ")", "{": "}"}
        for item in string:

            if item in bracket_map:
                stack.append(item)

            else:

                if len(stack) == 0:
                    return print(False)

                if item is bracket_map[stack[-1]]:
                    del stack[-1]

                else:
                    return print(False)

        if len(stack) > 0:
            return print(False)
        else:
            return print(True)

obj = Solution().isValid("(((())))()")