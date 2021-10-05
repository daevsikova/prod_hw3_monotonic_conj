import numpy as np
from os.path import isfile


def prepare_data(file_path):
    assert isfile(file_path), 'Data input file does not exist'
    
    num_lines = 0
    data = []
    
    with open(file_path, 'r') as f:
        for line in f:
            x, y = map(float, line.strip().split())
            data.append([x, y])
            num_lines += 1

    assert num_lines >= 9, 'Not enough data points. Method is applied for N >= 9'
    
    data = sorted(data, key=lambda x: x[0])
    return np.array(data)
