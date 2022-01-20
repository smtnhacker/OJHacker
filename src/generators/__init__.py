# LEs
from .genLE09 import le09
from .genLE10 import le10
from .genLE11 import le11
from .genLE12 import le12

#PAs
from .genPA04 import pa04
from .genPA05 import pa05
from .genPA06 import pa06
from .genPA07 import pa07
from .genPA08 import pa08

def none(checker = ""):
    return "No generator available", "No checker available"

class TCGenerator:
    """
    Test case generator class that facilitates creation of test case generators for every problem
    """
    _generators = {
        # Every [TYPE] maps to an array of generator functions where index is equal to [NUM]
        # Use placeholder function `none` for cases where the generator function is not yet available
        "PA" : [
            none, # Placeholder
            none, # PA01 - The Next Wesley So
            none, # PA02 - Shariki
            none, # PA03 - Hourglass Figure
            pa04, # PA04 - Podium Finish
            pa05, # PA05 - Goo Goo Ga Ga
            pa06, # PA06 - Carpet Laying
            pa07, # PA07 - Is there an error?
            pa08, # PA08 - P.I.
            none, # PA09 - Spaced Repetition
        ],

        "MP" : [
            none,
            none
        ],

        "LE" : [
            none, # Placeholder
            none, # LE01 - Recycling Paper
            none, # LE02 - Transferring Photos
            none, # LE03 - Team Drafting
            none, # LE04 - Sorting Fractions
            none, # LE05 - Ranking My Books
            none, # LE06 - Opteamization
            none, # LE07 - Student Council
            none, # LE08 - Simplifying Directions
            le09, # LE09 - Spatial Scanner
            le10, # LE10 - Pyramid Scheme
            le11, # LE11 - Converge to Self
            le12, # LE12 - Domain Expansion
        ]
    }
    def __init__(self, solutions):
        print("CREATED A TC GENERATOR")
        self._checkers = {
            # Every [TYPE] maps to an array of checker functions where index is equal to [NUM]
            # Use placeholder function `none` for cases where the checker function is not yet available
            "PA":[
                none, # Placeholder
                none,
                none,
                none,
                solutions.pa04,
                solutions.pa05,
                solutions.pa06,
                solutions.pa07,
                solutions.pa08,
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
                solutions.le09,
                solutions.le10,
                solutions.le11,
                solutions.le12,
            ],

            "MP":[
                none, # Placeholder
                none,
            ]
        }

    def create(self, TYPE, NUM):
        """
        Creates a function that generates a testcase for `problem`

        Parameter/s:
            TYPE (string) := Problem string in the form of either "LE", "PA", or "MP"
            NUM (int) := Problem number

        Return Value:
            function when called, outputs a test case for the given problem
        """
        print(f"TRYING TO GENERATE TC FOR {TYPE}{NUM}")
        generator = self._generators[TYPE][NUM](self._checkers[TYPE][NUM])
        res = generator()
        print(f"CREATED A {type(res)} : {res}")
        return res