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
        updated_location = dial.rotate(dial_input)

        if updated_location == 0:
            counter = counter + 1
            
    return f'(THIS IS THE NUMBER OF 0s!! {counter})'
