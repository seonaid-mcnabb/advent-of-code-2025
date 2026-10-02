import os
from day_2.IdHandler import IDHandler

def crack_the_code_day_2():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'day2input.csv')
    with open(file_path, 'r') as f:
        next(f)  # skip the "input" header
        range_inputs = f.read().strip().split(',')

    product = IDHandler()
    result = product.sum_invalid_ids(range_inputs)

    return result
