def stair():
    P = int(input())

    if(P<1 | P>20):
        print('Wrong Infrastructure')

    else:
        m = P // 2
        n = P % 2

        output = m + n + P
        print(output)
