import random

def le09(checker):
    def generator():
        def solved(a):
            sa = ""
            for i in a:
                if i == '*':
                    sa += (sa[0] if len(sa) >= 1 else "")
                elif i == '#':
                    sa = ((sa[1:] if len(sa) > 1 else ""))
                else:
                    sa += i
            return sa
        def stringGen(lnta):
            string_a, specs = "", ['*', '#']
            for j in range(lnta):
                rd = random.randint(1,4)
                if rd == 1:
                    q = random.randint(1,2)
                    string_a += specs[q%2]
                else:
                    q = random.randint(1,3)
                    if q == 1:
                        string_a += chr(random.randint(48,57))
                    elif q == 2:
                        string_a += chr(random.randint(65,90))
                    else:
                        string_a += chr(random.randint(97,122))
            return string_a
        TCS = random.randint(2,20)
        LST, specs = [str(TCS)], ['*', '#']
        for i in range(TCS):
            ans, qt = random.randint(1,2), random.randint(1,7)
            if qt == 3:
                LST.append(" ")
            elif qt == 4:
                string_c = ('#'*random.randint(1,5))+('*'*random.randint(0,3))+('#'*random.randint(0,4))+('*'*random.randint(2,7))
                LST.append(" "+string_c)
            elif qt == 5:
                string_c = ('#'*random.randint(1,5))+('*'*random.randint(0,3))+('#'*random.randint(0,4))+('*'*random.randint(2,7))
                LST.append(string_c+" ")
            elif qt == 5:
                string_c = stringGen(random.randint(5,20))
                LST.append(string_c+" ")
            else:
                if ans%2 == 0: #true
                    string_a, string_b = stringGen(random.randint(5,20)), ""
                    lntb = random.randint(0,len(string_a)+15)
                    for j in range(max(0,lntb-len(string_a))):
                        string_b += specs[random.randint(1,2)%2]
                    string_b += solved(string_a)
                    LST.append(string_a + " " + string_b)
                else:
                    LST.append(stringGen(random.randint(5,20)) + " " + stringGen(random.randint(0,20)))
        TC_LST = "\n".join(LST)
        TC_ANS = checker([str(i) for i in LST])
        return (TC_LST,TC_ANS)

    return generator