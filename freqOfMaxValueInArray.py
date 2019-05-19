#price = [2,1,2]
#query = [1,2,3]
# answer = [2,1,1,1,1]

#price = [2,2,2]
#query = [1,2,3]
# answer = [3,2,1]

#price = [2,1,2]
#query = [1,2,3]
# answer = [2,1,1]

dict = {}

#adding key and their count as values in dictionary
for i in price:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1
#print(dict)

#it's like giving max= -99999 but in this case giving infinity
maxVal = -float("inf")
maxArray = []

#adding max in array from last 
for i in range(len(price)-1,-1,-1):
    if price[i] > maxVal:
        maxVal = price[i]
    maxArray.append(maxVal)

maxArray.reverse()

res= []

#adding values in res by taking index of query
# query index starts from 0 and price index start from 1
#that is why price[i-1]

for i in query:
    if price[i-1] == maxArray[i-1]:
        res.append(dict[price[i-1]])
        dict[price[i-1]] = dict[price[i-1]] -1
    else:
        res.append(dict[price[i-1]])
        
print(res)

