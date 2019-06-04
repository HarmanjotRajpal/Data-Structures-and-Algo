matrix = [[1,1,0,1,0], [0,1,1,1,0],[1,1,1,1,0],[0,1,1,1,1]]
cache = []

m = len(matrix)
n = len(matrix[0])

#cloning value in matix in cache
for i in range(m):
    temp = []
    for j in range(n):
        temp.append(matrix[i][j])
    cache.append(temp)

result = 0

#calculating max square possible at i-th position
for i in range(1,m):
    for j in range(1,n):
        if i ==0  or j ==0:
            continue
        if matrix[i][j] > 0:
            cache[i][j] = cache[i][j] + min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1])
    
        if cache[i][j] > result:
            result = cache[i][j]
print(result)
