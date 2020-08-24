a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[], [], []]
for q in range(3):
    b = [[a[i][q] for i in range(2,-1,-1)] for q in range(3)]
print(b)
c = [[] for _ in range(3)]
print(c)