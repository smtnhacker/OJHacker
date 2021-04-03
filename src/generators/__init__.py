from .genPA04 import pa04

def none():
    return "No function available"

class TCGenerator:
    __generators = {
        "PA":[
            none, # Placeholder so index == PA #
            none,
            none,
            none,
            pa04,
        ]
    }
    def __init__(self, solutions):
        self.__checkers = {
            "PA":[
                none, # Placeholder
                none,
                none,
                none,
                solutions.pa04
            ]
        }

    def create(self, problem):
        '''
            Creates a function that generates a testcase for `problem`

            Parameter/s:
                problem (string) := Problem string in the form of TYPENUM (e.g. PA04, LE08)

            Return Value:
                function when called, outputs a test case for the given problem
        '''
        TYPE = problem[:2].upper()
        assert TYPE in ['PA', 'LE', 'MP']
        NUM = int(problem[2:])
        return self.__generators[TYPE][NUM](self.__checkers[TYPE][NUM])