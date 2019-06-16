
matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#len of row
m = len(matrix)

#len of column
n = len(matrix[0])

#starting index of row
k=0 
#starting index of column
l=0 


while k<m and l<n:
	#row
    for  i in range(l,n):
        print(matrix [k][i])
    k = k + 1
    
	#columm
    for i in range(k,m):
        print(matrix[i][n-1])
    n=n-1
    
	#last row
    for i in range(n-1,l-1,-1):
        print(matrix[m-1][i])
    m = m-1

	#reverse column

        print(matrix[i][l])
    l = l+1
