#flipping an image
image= [[1,1,0],[1,0,1],[0,0,0]]
new = []
for i in image:
	i.reverse()
	new.append(i)
#print(new)
m  = len(new) #row
n = len(new[0]) # col

for item in new:
    for i in range(0,m):
        for j in range(0,n):
            if new[i][j] == 0:
                new[i][j] = 1 
            else: 
                new[i][j] = 0 
print(new)
