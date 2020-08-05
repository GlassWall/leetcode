from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        prices = defaultdict(lambda:sys.maxsize)
        for s,d,c in flights:
            graph[s].append([d,c])
            prices[s]
            prices[d]
        q = [(src,-1,0)]
        while q:
            cur,k,cost = q.pop(0)
            if k==K or cur==dst:
                continue
            for dest,cost2 in graph[cur]:
                if cost + cost2 < prices[dest]:
                    prices[dest] = cost + cost2
                    q.append((dest,k+1,cost+cost2))
        if prices[dst] != sys.maxsize:
            return prices[dst]
        else:
            return -1