import heapq as hq

list_values = [2,0,2,3]
hq.heappush(list_values, 9)
ns = hq.heappop(list_values)
print(ns)