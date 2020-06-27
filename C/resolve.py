def resolve():
    '''
    code here
    '''

    N, M, K = [int(item) for item in input().split()]
    As = [int(item) for item in input().split()]
    Bs = [int(item) for item in input().split()]

    res = 0
    time = 0

    memo_A = [0]
    for i in range(N):
        memo_A.append(As[i]+memo_A[-1])

    memo_B = [0]
    for i in range(M):
        memo_B.append(Bs[i]+memo_B[-1])

    res = 0
    j = M
    for i, av in enumerate(memo_A):
        if av > K:
            break
        else:
            
            while av + memo_B[j] > K:
                j -= 1
            res = max(res,j+i)

    print(res)

if __name__ == "__main__":
    resolve()
            
