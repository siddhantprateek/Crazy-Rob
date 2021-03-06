#  you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer


def square_digits(number):
    new_number = int(0)

    while number != 0:
        power = len(str(number)) - 1
        sqr = number // 10**power
        real_sqr = sqr**2
        value = len(str(real_sqr))
        new_number = new_number*10**value + real_sqr
        number = number % 10**power

    print(new_number)


square_digits(9119)
square_digits(123)
square_digits(456)
