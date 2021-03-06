def maxPoints(points: list[list[int]]):
    num_cordinate = len(points)

    cordinate_1, cordinate_2, *rest = points
    slope = cordinate_1[1] - cordinate_2[1] / cordinate_1[0] - cordinate_2[1]
