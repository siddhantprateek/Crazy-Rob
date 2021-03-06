
# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))


# matrix = []


# for i in range(R):
#     a = []
#     for j in range(C):
#         a.append(int(input()))
#     matrix.append(a)

# for i in range(R):
#     for j in range(C):
#         print(matrix[i][j], end=" ")
#     print()

# OR


r, c = 4, 4

matrix = []
for i in range(r):
    x = input()
    matrix.append(x.split())