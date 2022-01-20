import random

def pa07(checker):
    def generator():
        N = random.randint(1, 123456789) % 9000 + 1000
        TCS = str(N)
        ANSWERS = str(checker(N))
        return (TCS, ANSWERS)
    return generator