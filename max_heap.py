
import heapq

#max heap
l = []

heapq.heappush(l,-(20))
heapq.heappush(l,-(10))
heapq.heappush(l,-(30))
heapq.heappush(l,-(1))
heapq.heappush(l,-(3))
heapq.heappush(l,-(-2))

heapq.heapify(l)
print('heapify', l)

h = -(heapq.heappop(l))
print('max element', h)


#min heap 
li = []
heapq.heappush(li ,(20))
heapq.heappush(li ,(10))
heapq.heappush(li ,(30))
heapq.heappush(li ,(1))
heapq.heappush(li ,(3))
heapq.heappush(li ,(-2))

heapq.heapify(li)
print('heapify', li)

m = heapq.heappop(li)
print('min element', m)
