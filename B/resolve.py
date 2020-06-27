def resolve():
    '''
    code here
    '''
    S = input()
    T = input()

    cnt = 0
    for i, v in enumerate(S):
        if v != T[i]:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    resolve()
