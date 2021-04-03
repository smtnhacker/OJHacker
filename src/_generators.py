import random
import _solutions

randNames = [
    'William', 'Elijah', 'James', 'Benjamin', 'Lucas',
    'Mason', 'Ethan', 'Alexander', 'Henry', 'Jacob',
    'Michael', 'Daniel', 'Logan', 'Jackson', 'Sebastian',
    'Jack', 'Aiden', 'Owen', 'Samuel', 'Matthew',
    'Joseph', 'Levi', 'Mateo', 'David', 'John',
    'Wyatt', 'Carter', 'Julian', 'Luke', 'Grayson',
    'Isaac', 'Jayden', 'Theodore', 'Gabriel', 'Anthony',
    'Dylan', 'Leo', 'Lincoln', 'Jaxon', 'Asher',
    'Christopher', 'Josiah', 'Andrew', 'Thomas', 'Joshua',
    'Ezra', 'Hudson', 'Charles', 'Caleb', 'Isaiah',
    'Ryan', 'Nathan', 'Adrian', 'Christian', 'Maverick',
    'Colton', 'Elias', 'Aaron', 'Eli', 'Landon',
    'Jonathan', 'Nolan', 'Hunter', 'Cameron', 'Connor',
    'Santiago', 'Jeremiah', 'Ezekiel', 'Angel', 'Roman',
    'Easton', 'Miles', 'Robert', 'Jameson', 'Nicholas',
    'Greyson', 'Cooper', 'Ian', 'Carson', 'Axel',
    'Jaxson', 'Dominic', 'Leonardo', 'Luca', 'Austin',
    'Jordan', 'Adam', 'Xavier', 'Jose', 'Jace',
    'Everett', 'Declan', 'Evan', 'Kayden', 'Parker',
    'Wesley', 'Kai', 'Brayden', 'Bryson', 'Weston',
    'Jason', 'Emmett', 'Sawyer', 'Silas', 'Bennett',
    'Brooks', 'Micah', 'Damian', 'Harrison', 'Waylon',
    'Ayden', 'Vincent', 'Ryder', 'Kingston', 'Rowan',
    'George', 'Luis', 'Chase', 'Cole', 'Nathaniel',
    'Zachary', 'Ashton', 'Braxton', 'Gavin', 'Tyler',
    'Diego', 'Bentley', 'Amir', 'Beau', 'Gael',
    'Carlos', 'Ryker', 'Jasper', 'Max', 'Juan',
    'Ivan', 'Brandon', 'Jonah', 'Malachi', 'Milo',
    'Emmanuel', 'Karter', 'Rhett', 'Alex', 'August',
    'River', 'Xander', 'Antonio', 'Brody', 'Finn',
    'Elliot', 'Dean', 'Emiliano', 'Eric', 'Miguel',
    'Arthur', 'Matteo', 'Graham', 'Alan', 'Nicolas',
    'Blake', 'Thiago', 'Adriel', 'Victor', 'Joel',
    'Timothy', 'Hayden', 'Judah', 'Abraham', 'Edward',
    'Messiah', 'Zayden', 'Theo', 'Tucker', 'Grant',
    'Richard', 'Alejandro', 'Steven', 'Jesse', 'Dawson',
    'Bryce', 'GabSamonte', 'MikoSurara', 'ClydeFrongoso',
]

def genPA05():
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
  ans_tc = solutions.ans_PA05([str(i) for i in generated_tc])
  return (tc, ans_tc)

def genPA04():
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
  forms = ['sec', 'min_sec', 'hour_min_sec']
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
  ans = solutions.ans_PA04([str(i) for i in genLST])
  return (tc,ans)

def genPA06():
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
  TC_ANS = solutions.ans_PA06([str(i) for i in lst])
  return (TC_LST, TC_ANS)

def genLE08():
  DIRECTIONS = ['UP', 'DOWN', 'LEFT', ' RIGHT']
  LST = []
  TCS = random.randint(2,20)
  LST.append(str(TCS))
  for j in range(TCS):
    x = random.randint(4, 20)
    s = ""
    for i in range(x):
        qt = random.randint(1,4)
        s += DIRECTIONS[qt%4] + " "
    LST.append(s)
  TC_LST = "\n".join([str(i) for i in LST])
  TC_ANS = solutions.ans_LE08([str(i) for i in LST])
  return (TC_LST, TC_ANS)

def genLE07():
    inp = []
    N = random.randint(1,30)
    inp.append(str(N))

    number_of_cand = random.randint(1,30)
    shuffled = randNames[:]
    random.shuffle(shuffled)

    people_list = shuffled[:N]
    cand_list = shuffled[:number_of_cand]

    pos = ["pres", "vp", "sec", "mc", "prc", "swc", "sr"]

    should_be_weird = random.randint(1,4)
    if should_be_weird == 1:
      N = random.randint(2,7)
      inp[0] = str(N)
      number_of_cand = random.randint(1, 7)
      shuffled = pos[:]
      random.shuffle(shuffled)

      people_list = shuffled[:N]
      cand_list = shuffled[:number_of_cand]
    
    for i in range(N):
        person = people_list[i]
        mask = random.randint(0,127)
        voted = []

        for j in range(7):
            if mask & (1 << j):
                voted_person = cand_list[random.randint(0,number_of_cand-1)]
                voted.append(pos[j] + " " + voted_person)

        inp.append(person + " " + " ".join(voted))

    TC_INP = "\n".join(i for i in inp)
    TC_ANS = solutions.ans_LE07(inp)
    return (TC_INP, TC_ANS)

def genLE09():
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
  TC_ANS = solutions.ans_LE09([str(i) for i in LST])
  return (TC_LST,TC_ANS)
