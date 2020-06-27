def resolve():
    '''
    code here
    '''
    import math

    N = int(input())

    def get_sieved_list(x):
        dp = [1 if item % 2 == 0 else 0 for item in range(x+1)]
        dp[:3] = [2,1,1]

        for prim_candi in range(3, x+1):
            temp_num = prim_candi
            while temp_num <= x:
                dp[temp_num] += 1
                temp_num += prim_candi
            if prim_candi >= x:
                return [i  for i in range(x+1) if dp[i] == 1]


    def num_factor(num):
        if num == 1:
            return 1
        else:
            factor_dict = zip(get_sieved_list(N), [0]*len(get_sieved_list(N)))

            for i in factor_dict.keys():
                if num % i == 0:
                    factor_dict[i] = num // i

            cnt = 1
            for item in factor_dict.values()[1:]:
                cnt *= item
        return item

    res = 0
    for i in range(1, N+1):
        res += i*num_factor(i)

    print(res)
            


if __name__ == "__main__":
    resolve()
