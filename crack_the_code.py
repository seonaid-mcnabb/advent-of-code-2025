import pandas as pd
import os
from Dial import Dial, DialInput

def crack_the_code():
    dial = Dial(50)

    base_dir = os.path.dirname(__file__)  # directory where this script lives
    file_path = os.path.join(base_dir, 'puzzleinput.csv')

    df = pd.read_csv(file_path)
    rotation_inputs = df['input'].tolist()
    counter = 0

    for input in rotation_inputs:
        dial_input = DialInput(input)

        # 

        zeros_passed = dial.count_zero_passes(dial_input)
        if zeros_passed > 0:
            counter = counter + zeros_passed
        updated_location = dial.rotate(dial_input)

        # CURRENTLY -- the updated location code returns the number of times the rotation LANDS on 0
        if updated_location == 0:
            counter = counter + 1
            
    return f'(THIS IS THE NUMBER OF 0s!! {counter})'
