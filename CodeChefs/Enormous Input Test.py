
# (n, k) = map(int, input().split(' '))
n, k = [str(item) for item in input().split()]
n, k = int(n), int(k)
def count(n, k):
    count_the_divisible = 0
    while n > 0:
        get = int(input())
        if get%k == 0:
            count_the_divisible += 1
            n -= 1
    return count_the_divisible
count(n, k)

(n, k) = map(int, intput().split(' '))

count_the_divisible = 0
for _ in range(n):
    get = int(input())
    if get%k == 0:
        count_the_divisible += 1
print(count_the_divisible)

