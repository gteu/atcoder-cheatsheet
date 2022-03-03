def dij(G, s):
    """Dijkstra's algorithm
    Args:
        G (List[List[int, int]]): [adjacent node, weight] 
        s (int): starting index

    Returns:
        d (List[int]): distances
    """
    from heapq import heappush, heappop

    d = [INF] * len(G)
    d[s] = 0
    q = [(0, s)]
    while q:
        cur_d, cur_i = heappop(q)
        if cur_d > d[cur_i]:
            continue
        for nxt_i, w, k in G[cur_i]:
            nxt_d = cur_d + w + (- cur_d % k)
            if d[nxt_i] > nxt_d:
                d[nxt_i] = nxt_d
                heappush(q, (nxt_d, nxt_i))
    return d


INF = 10 ** 18
N, M, X, Y = map(int, input().split())
X -= 1
Y -= 1
to = [[] for _ in range(N)]
for _ in range(M):
    A, B, T, K = map(int, input().split())
    A -= 1
    B -= 1
    to[A].append([B, T, K])
    to[B].append([A, T, K])

d = dij(to, X)
if d[Y] == INF:
    print(-1)
else:
    print(d[Y])
