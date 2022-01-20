import random

def pa06(checker):
    def generator():
        lst, MAXN = [], 1000000
        tcs = random.randint(1,10)
        lst.append(tcs)
        for i in range(tcs):
            N = random.randint(1,10)
            lst.append(N)
            fakeLST, randMod = [], [100,1000,10000,10000]
            for j in range(N):
                rFactor, newFactor = random.randint(1,3), random.randint(1,4)
                a = random.randint(2,500000)%randMod[newFactor%4]
                b = random.randint(a+2,MAXN)%randMod[newFactor%4]
                if b < a:
                    a, b = b, a
                if b == a:
                    b += 1
                if rFactor%4 == 1 and j != 0:
                    fakeLST.append(fakeLST[-1])
                else:
                    fakeLST.append(str(a)+" "+str(b))
                random.shuffle(fakeLST)
            for k in fakeLST:
                lst.append(k)
        TC_LST = "\n".join([str(i) for i in lst])
        TC_ANS = checker([str(i) for i in lst])
        return (TC_LST, TC_ANS)

    return generator