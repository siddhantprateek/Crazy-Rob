import math


def area(r):
    return math.pi*(r**2)


radii = [2, 4, 5, 6]

areas = []
for r in radii:
    a = area(r)
    areas.append(a)
print(areas)


# areas = map(lambda r: math.pi*(r**2), radii)
# print(list(areas))

# the map function takes two argument
# map( <function>, <list/ tuple /or iterable objects>)
print(list(map(lambda r: math.pi*(r**2), radii)))
