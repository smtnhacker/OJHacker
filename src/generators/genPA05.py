import random

def pa05(checker):
    def generator():
        generated_tc = []
        TCS = random.randint(1, 5)
        
        generated_tc.append(TCS)
        for i in range(TCS):
            N = 2 * random.randint(1, 8)
            generated_tc.append(N)
            for j in range(N):
                M = random.randint(1, 20)
                ST = ""
                for k in range(M):
                    ST += str(chr(random.randint(65, 90)))
                generated_tc.append(ST)
        tc = "\n".join([str(i) for i in generated_tc])
        ans_tc = checker([str(i) for i in generated_tc])
        return (tc, ans_tc)

    return generator