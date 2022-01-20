import random
from .locations import locations

def pa08(checker):

    def generator():
        THRESHOLD = min(30, len(locations))
        generated_input = []

        def print_(x):
            generated_input.append(x)

        print_("---")
        
        # this is generated the way that the tcs in
        # the OJ are thought to be generated

        shuffled_loc = locations[:]
        random.shuffle(shuffled_loc)

        common_len = random.randint(0, THRESHOLD)
        common_places = shuffled_loc[-common_len:]
        del shuffled_loc[-common_len:]

        loc = [
            common_places[:],
            common_places[:],
            common_places[:],
        ]

        n_left = THRESHOLD - common_len

        for i in range(3):
            unique_len = random.randint(0, n_left)
            n_left -= unique_len
            loc[i] += shuffled_loc[-unique_len:]
            del shuffled_loc[-unique_len:]

            random.shuffle(loc[i])
            for x in loc[i]:
                print_(x)
            print_("---")

        input_tc = "\n".join(str(x) for x in generated_input)
        output_tc = checker([str(x) for x in generated_input])
        return (input_tc, output_tc)

    return generator