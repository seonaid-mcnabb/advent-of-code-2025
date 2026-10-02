import os
from day_2.IdHandler import IDHandler

def crack_the_code_day_2():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'day2input.csv')
    with open(file_path, 'r') as f:
        next(f)  # skip the "input" header
        range_inputs = f.read().strip().split(',')

    product = IDHandler()
    result = product.filter_invalid_ids(range_inputs)

    print(result)
    assert result == 0
    return result
