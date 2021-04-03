import random
# IF NAMES ARE TO BE GENERATED
from .names import randNames

def typeNum(checker):
    '''
        Creates a function that generates a 2-tuple testcase containing the input and output

        Parameters:
            checker (function) := checker function that generates the output string based on the generated input

        Return:
            function
    ''' 

    def generator():
        '''
            Returns a 2-tuple testcase (INPUT: string, OUTPUT: string)

            Note that, compared to the previous generator format, instead of invoking solutions.ans_TYPENUM call checker instead
        '''
        pass

    return generator