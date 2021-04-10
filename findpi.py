import random
def estimate_pi(n):
    num_point_circle, num_point_square = 0, 0

    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
        num_point_square += 1

    return 4*(num_point_circle / num_point_square)
'''
The uniform() method returns a random floating number between the two specified numbers (both included).
'''
n = 1
trails = 0 
while True:
    pi = estimate_pi(n)
    n += 1
    if pi == 3.14:
        break
    trails += 1
print(pi, "trail: ", trails)

