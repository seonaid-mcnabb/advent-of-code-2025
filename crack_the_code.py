import pandas as pd
import os
from day1.Dial import Dial

def crack_the_code():
    dial = Dial(50)

    base_dir = os.path.dirname(__file__)  # directory where this script lives
    file_path = os.path.join(base_dir, 'puzzleinput.csv')

    df = pd.read_csv(file_path)
    rotation_inputs = df['input'].tolist()
    counter = 0

    for input in rotation_inputs:
        dial.rotate(input)
        updated_location = dial.current_location
        if updated_location == 0:
            counter = counter + 1

    return f'(THIS IS THE NUMBER OF 0s!! {counter})'
