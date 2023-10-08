import numpy as np


def read_data(file):
    text = np.genfromtxt(file, delimiter='\n', dtype=np.bytes_)
    decoded_text = np.char.decode(text)
    # TODO
    return # TODO


def get_line_lengths(array):
    return # TODO


if __name__ == '__main__':
    uppercase_text = read_data('text.txt')
    line_lengths = get_line_lengths(uppercase_text)
    print(uppercase_text)
    print(line_lengths)
