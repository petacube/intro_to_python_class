#The expected output is not a label, or even a set of labels, but a colored grid
#with size up to 30x30, and with up to 10 different colors. It therefore falls in
#the domain of structured prediction [3].
#The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

#"train": demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
#"test": test input/output pairs. It is a list of "pairs" (typically 1 pair).
#A "pair" is a dictionary with two fields:

#"input": the input "grid" for the pair.
#"output": the output "grid" for the pair.
#A "grid" is a rectangular matrix (list of lists) of integers between 0 and 9 (inclusive).
# The smallest possible grid size is 1x1 and the largest is 30x30.

#When looking at a task, a test-taker has access to inputs & outputs of the demonstration pairs,
# plus the input(s) of the test pair(s).
# The goal is to construct the output grid(s) corresponding to the test input grid(s), using 3 trials for each test input.
# "Constructing the output grid" involves picking the height and width of the output grid,
# then filling each cell in the grid with a symbol (integer between 0 and 9, which are visualized as colors).
# Only exact solutions
#(all cells match the expected answer) can be said to be correct.
import numpy as np
import json as js
import sys
# data from here
# input data is
import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolor
import copy
import glob

from color_mgmt import *
from arc_challenge_utils import *

print(os.getcwd())

training_path = r"ARC-AGI-master\data\training"
json_files = glob.glob(os.path.join(training_path, "*.json"))
# we only know one concept - containment - we will add more concepts
file_to_concept_map = {"containment":"00d62c1b.json"}

json_files = list(filter(lambda x: file_to_concept_map['containment'] in x,json_files))

for json_file in json_files:
    data = js.load(open(json_file,"r"))
    case_number =0
    for train_sample in data['train']:
        case_number +=1
        if case_number >0:
            input=train_sample['input']
            output = train_sample['output']
            input_arr = np.array(input).flatten().reshape(len(input),len(input))
            output_arr = np.array(output).flatten().reshape(len(input), len(input))

            # basic solution
            # define a concept of cell containment

            #always display input first
            visualize_array(input_arr)


            computed_output = apply_concept(input_arr)
            if  np.array_equal(computed_output, output_arr):
                print("matches!!")
            else:
                print("wrong answer")
                visualize_array(input_arr)
                visualize_array(output)
                visualize_array(computed_output)


