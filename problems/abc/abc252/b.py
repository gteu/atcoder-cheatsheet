N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(N):
    if A[i] == max(A) and i + 1 in B:
        print('Yes')
        exit()
print('No')
