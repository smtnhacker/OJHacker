import random

def pa07(checker):
    def generator():
        generated_input = []
        
        # insert logic here

        input_tc = "\n".join([str(i) for i in generated_input])
        output_tc = checker([str(i) for i in generated_input])
        return (input_tc, output_tc)

    return generator