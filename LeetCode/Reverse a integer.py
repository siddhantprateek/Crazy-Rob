
def reverse():
    number = int(input())
    reverse = int(0)
    if number > 0:
        while number != 0:
            reminder = number % 10
            reverse = reverse*10 + reminder
            number = number // 10  # FLOOR DIVISION IS ALSO INTEGER DIVISION
            #print(reverse)
        print(reverse)
    else:
        negative = -number
        while negative != 0:
            reminder = negative % 10
            reverse = reverse*10 + reminder
            negative = negative // 10  # FLOOR DIVISION IS ALSO INTEGER DIVISION
            #print(-reverse)
        print(-reverse)


reverse()
