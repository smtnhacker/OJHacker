import random

def le12(checker):

    def generator():
        generated_tc = []
        N = random.randint(1, 10)
        generated_tc.append(str(N))
        for i in range(N):
            to_add = random.randint(0, 12)
            current_tc = ""
            n_open = 0
            n_close = 0
            for j in range(to_add):
                case = random.randint(1, 10000) % 4
                if case == 3: # open parenthesis
                    n_open += 1
                    current_tc += "("
                elif case == 1 and n_close < n_open: # close parenthesis
                    n_close += 1
                    current_tc += ")"
                else: # letter num combo
                    letter = chr(ord('A') + random.randint(0, 9))
                    number = random.randint(1, 9)
                    current_tc += str(letter) + str(number)
            while n_open > n_close:
                n_close += 1
                current_tc += ")"
            generated_tc.append(current_tc)
        TCS = "\n".join(generated_tc)
        ANSWERS = checker(generated_tc)
        return (TCS, ANSWERS)

    return generator