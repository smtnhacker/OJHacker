import random
from .names import randNames

def pa04(checker):
    def generator():
        def sums(n):
            return (n*(n+1))//2
        #basta return prongs na tuple (str nung tc, str nung ans)
        genLST, vis, GL = [], {}, []
        people, laps = random.randint(5,10), random.randint(2,5)
        random.shuffle(randNames)
        collectedNames = []
        genLST.append(people)
        genLST.append(laps)
        for i in range(people):
            collectedNames.append(randNames[i])
        forms = ['sec','min_sec','hour_min_sec']
        for i in range(people):
            for j in range(laps):
                randF, nums = random.randint(1,3), 0
                if randF-1 == 0:
                    nums = str(random.randint(1,5000000))
                elif randF-1 == 1:
                    nums = str(random.randint(1,59))+":"+str(random.randint(1,59))
                else:
                    nums = str(random.randint(1,1000000))+":"+str(random.randint(1,59))+":"+str(random.randint(1,59))
                genLST.append(collectedNames[i]+" "+str(j+1)+" "+forms[randF-1]+" "+nums)
                GL.append(collectedNames[i]+" "+str(j+1)+" "+forms[randF-1]+" "+nums)
        random.shuffle(GL)
        tc = str(people)+" "+str(laps)+"\n"
        tc += "\n".join([str(i) for i in GL])
        ans = checker([str(i) for i in genLST])
        return (tc,ans)

    return generator