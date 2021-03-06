def PascalsTriangle(number):

    for spaces in reversed(range(number)):
        print(" "*spaces, "*"*(number - spaces),
              "*"*(number - spaces), " "*(spaces))


PascalsTriangle(10)
