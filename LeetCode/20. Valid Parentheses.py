def isValid(s: str):


    Open_brackets, brackets = [] , {'(': ')', '[': ']', '{': '}' }

    for item in s:
        if item in brackets:
            Open_brackets.append(item)
        elif not Open_brackets or brackets[Open_brackets.pop()] != item:
            print()
            return print(False)

    return print(not Open_brackets)

isValid("()")