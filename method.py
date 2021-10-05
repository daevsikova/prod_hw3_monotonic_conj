import numpy as np
from utils import prepare_data
from argparse import ArgumentParser
from scipy.stats import rankdata


def monotonic_conj(input_path, output_path):
    data = prepare_data(input_path)
    N = data.shape[0]
    
    ranks = rankdata(data[:, 1], method="average")
    ranks = -ranks + N + 1

    p = int(round(N / 3))
    
    R1 = np.sum(ranks[:p])
    R2 = np.sum(ranks[-p:])

    diff = R1 - R2
    err = (N + 0.5) * (p / 6) ** 0.5
    conj = diff / (p * (N - p))

    # saving results
    with open(output_path, 'w') as f:
        f.write(f"{round(diff)} {round(err)} {round(conj, ndigits=2)}")


if __name__ == "__main__":
    parser = ArgumentParser(description="Testing of monotonic conjugation")
    parser.add_argument("--input_path", default="in.txt")
    parser.add_argument("--output_path", default="out.txt")
    args = parser.parse_args()

    monotonic_conj(args.input_path, args.output_path)
    