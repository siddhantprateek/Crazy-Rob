def factorial(number: int):
    fact = 1
    while number > 0:
        fact *= number
        number -= 1
    print(fact)


factorial(5)
factorial(0)
