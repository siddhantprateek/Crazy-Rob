def PascalsTriangle(number):

    for spaces in reversed(range(number)):
        print(" "*spaces, "*"*(number - spaces),
              " "*spaces, "*"*(number - spaces),
              " "*spaces, "*"*(number - spaces))
    for spaces in reversed(range(number)):
        print(" "*(number - spaces), "*"*spaces,
              " "*(number - spaces), "*"*spaces,
              " "*(number - spaces), "*"*spaces)


PascalsTriangle(10)
