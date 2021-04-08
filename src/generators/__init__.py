from .genPA04 import pa04
from .genPA05 import pa05

def none(checker = ""):
    return "No generator available", "No checker available"

class TCGenerator:
    '''
        Test case generator class that facilitates creation of test case generators for every problem

    '''
    __generators = {
        # Every [TYPE] maps to an array of generator functions where index is equal to [NUM]
        # Use placeholder function `none` for cases where the generator function is not yet available
        "PA" : [
            none,
            none,
            none,
            none,
            pa04,
            pa05,
            none,
            none,
            none,
            none,
        ],

        "MP" : [
            none,
            none
        ],

        "LE" : [
            none,
            none,
            none,
            none,
            none,
            none,
            none,
            none,
            none,
            none,
            none,
            none,
        ]
    }
    def __init__(self, solutions):
        print("CREATED A TC GENERATOR")
        self.__checkers = {
            # Every [TYPE] maps to an array of checker functions where index is equal to [NUM]
            # Use placeholder function `none` for cases where the checker function is not yet available
            "PA":[
                none, # Placeholder
                none,
                none,
                none,
                solutions.pa04,
                solutions.pa05,
                none,
                none,
                none,
                none,
                none,
                none,
                none,
            ],

            "LE":[
                none, # Placeholder
                none,
                none,
                none,
                none,
                none,
                none,
                none,
                none,
                none,
                none,
                none,
                none,
            ],

            "MP":[
                none, # Placeholder
                none,
            ]
        }

    def create(self, TYPE, NUM):
        '''
            Creates a function that generates a testcase for `problem`

            Parameter/s:
                TYPE (string) := Problem string in the form of either "LE", "PA", or "MP"
                NUM (int) := Problem number

            Return Value:
                function when called, outputs a test case for the given problem
        '''
        print(f"TRYING TO GENERATE TC FOR {TYPE}{NUM}")
        generator = self.__generators[TYPE][NUM](self.__checkers[TYPE][NUM])
        res = generator()
        print(f"CREATED A {type(res)} : {res}")
        return res