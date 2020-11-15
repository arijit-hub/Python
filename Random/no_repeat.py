def non_repeat():

    S = input().lower()
    if((len(S) < 1) or (len(S) > 20)):
        print('Wrong Input')
    else:
        for i in range(len(S)):
            if(i == 0):
                m = S.find(S[i] , i + 1)
                if(m == -1):
                    print(S[i])
                    break
            elif(i == len(S) - 1):
                m = S.rfind(S[i] , i - 1)
                if(m == -1):
                    print(S[i])
                    break
            else:
                m = S.find(S[i] , i + 1)
                n = S.rfind(S[i] , i - 1)

                if(m == -1 and n == -1):
                    print(S[i])
                    break

        if(m != -1):
            print('Exceptional String')
    
