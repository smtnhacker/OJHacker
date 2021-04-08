import random
from .names import randNames

def le10(checker):
    def generator():
        THRESHOLD = 50
        MAX_MONEY = 1000000
        generated_input = []

        vis = list()
        def dfs(n, members, x):
            if x >= n or members[x] == '':
                return
            if x > 0:
                vis.append(x)
            dfs(n, members, 2*x + 1)
            dfs(n, members, 2*x + 2)

        def print_(x):
            generated_input.append(x)

        N = random.randint(2, THRESHOLD)

        members = list(filter(lambda x : x != 'Bob', randNames))
        random.shuffle(members)
        members = members[:N]
        members[0] = 'Bob'

        probability_set = set(range(10, 20))
        for i in range(3, N):
            is_nobody = random.randint(1,100) in probability_set
            if is_nobody:
                members[i] = ''

        commissions = [round(random.uniform(0.01,0.99), 5) for _ in range(N)]
        principal_money = [random.randint(1, MAX_MONEY) for _ in range(N)]

        dfs(N, members, 0)
        members[random.choice(vis)] = 'YOU'

        print_(f"members = {members}")
        print_(f"commissions = {commissions}")
        print_(f"principal_money = {principal_money}")
        print_(f"result = recurse(members, commissions, principal_money, 0, False)")

        input_tc = "\n".join(generated_input)
        output_tc = str(checker(members, commissions, principal_money, 0, False))
        return (input_tc, output_tc)

    return generator