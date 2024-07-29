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
from math import ceil
from color_mgmt import *
def compute_slab_distance(slab,direction):
    condition = lambda x: x ==  color_to_num_map['green']
    pos = np.where(condition(slab))
    if len(pos) > 0:
        if len(pos[0]) >0:
        # distance is counted from end of the list
            if (direction == "top"):
                return len(slab) - pos[0][-1]
            elif (direction == "left"):
                return len(slab) - pos[0][-1]
            elif (direction == "right"):
                return 1+pos[0][0]
            elif (direction == "bottom"):
                return 1+pos[0][0]
            else:
                raise Exception(f"unknwon direction {direction}")
        else:
            return -1
    else:
        return -1

# parent cells is list of indexes that been explored before
def cell_contained(in_window=None, i=0, j=0, parent_cells=[],debug=False):
    contained_list=[]
    """
    
    @param in_window: 
    @param i: 
    @param j: 
    @param parent_cells: 
    @return: tuple, if cell is contained and list of other cells which has been disccovered to be contained
     
    """
    if debug:
        print(f"processing {i},{j} for parent cells of {parent_cells}")
        visualize_array(in_window,i,j,parent_cells)
    if num_to_color_map[in_window[i,j]] == 'green':
        raise Exception(f"not supposed to be here {i},{j} cause it green")
    if (color_to_num_map['green'] in in_window[:i,j] and  \
        color_to_num_map['green'] in in_window[(i+1):,j] and \
        color_to_num_map['green'] in in_window[i,:j] and  \
        color_to_num_map['green'] in in_window[i,(j+1):]):
        top_distance = compute_slab_distance(in_window[:i,j],direction="top")
        # assymetry in python end range not included but right one is
        bottom_distance= compute_slab_distance(in_window[(i+1):,j],direction="bottom")
        left_distance = compute_slab_distance(in_window[i,:j],direction="left")
        # aware of assymetry
        right_distance = compute_slab_distance(in_window[i,(j+1):],direction="right")
        if (top_distance == 1) and \
                (bottom_distance == 1) and \
                (left_distance == 1) and \
                (right_distance == 1):
                return True,contained_list
        else:
            #
            #We are searching for first nearest empty cell that not contained
            #
            if debug:
                print(f"top distance is {top_distance}, bottom {bottom_distance}, left is {left_distance}, right is {right_distance}")
            parent_cells.append((i,j))

            #visualize_array(in_window,i,j,parent_cells)
            if top_distance >1:
                for k in range(i-top_distance+1,i):
                    # dont look at parents cells
                    if (k,j) not in parent_cells:
                        if debug:
                            print("top processing")
                        is_top_contained, child_contained_list = cell_contained(in_window,k,j, parent_cells)
                        if not is_top_contained:
                            return False,contained_list + child_contained_list
                        else:
                            # memorize result
                            contained_list.append((k,j))
            if bottom_distance >1:
                for k in range(i+1,i+bottom_distance):
                    if (k,j) not in parent_cells:
                        if debug:
                            print("bottom procesing")
                        is_bottom_contained, child_contained_list =  cell_contained(in_window,k,j,parent_cells)
                        if not is_bottom_contained:
                            return False,contained_list + child_contained_list
                        else:
                            # memorize result
                            contained_list.append((k,j))
            if left_distance >1:
                for k in range(j-left_distance+1,j):
                    if (i,k) not in parent_cells:
                        if debug:
                            print("left procesing")
                        is_left_contained, child_contained_list =  cell_contained(in_window,i,k,parent_cells)
                        if not is_left_contained:
                            return False,contained_list + child_contained_list
                        else:
                            # memorize result
                            contained_list.append((i,k))
            if right_distance >1:
                for k in range(j+1,j+right_distance):
                    if (i,k) not in parent_cells:
                        if debug:
                            print("right processing")
                        is_right_contained, child_contained_list = cell_contained(in_window,i,k,parent_cells)
                        if not is_right_contained:
                            return False,contained_list + child_contained_list
                        else:
                            # memorize result
                            contained_list.append((i,k))

            return True,contained_list

    else:
        return False,contained_list

def apply_concept(in_window,debug=False):
    contained_cache=set()
    out_window = np.zeros(in_window.shape)
    i_max, j_max = in_window.shape
    for i in range(i_max):
        for j in range(j_max):
            if num_to_color_map[in_window[i,j]] == 'green':
                # copy
                out_window[i,j] = in_window[i,j]
            elif num_to_color_map[in_window[i,j]] == 'black':
                # check for containment
                if (i,j) in contained_cache:
                   out_window[i,j] = color_to_num_map['yellow']
                else:
                    is_contained, contained_list = cell_contained(in_window,i,j,[],debug)
                    list(map(lambda elem: contained_cache.add(elem),contained_list))
                    if is_contained:
                        out_window[i,j] = color_to_num_map['yellow']

    return out_window

def apply_stripped_mirror(in_window,debug=False):
    colored_cells_pos=[]
    out_window = np.zeros(in_window.shape)
    #scan
    i_max, j_max = in_window.shape
    for i in range(i_max):
        for j in range(j_max):
            if in_window[i,j] != 0:
                # copy
                colored_cells_pos.append((i,j,in_window[i,j]))

    horizontal_distance = abs(colored_cells_pos[0][1] - colored_cells_pos[1][1])
    vertical_distance = abs(colored_cells_pos[0][0] - colored_cells_pos[1][0])

    for i,j,color in colored_cells_pos:
        if (i == 0):
            #mirror horizontally
            num_stripes = ceil((j_max-j)/(2*horizontal_distance))
            for k in range(num_stripes):
                next_pos = j + k*2*horizontal_distance
                out_window[:,next_pos] = color
        elif (i == i_max-1):
            num_stripes = ceil((j_max-j)/(2*horizontal_distance))
            for k in range(num_stripes):
                next_pos = j + k*2*horizontal_distance
                out_window[:,next_pos] = color
        elif (j == 0):
              num_stripes = ceil((i_max-i)/(2*vertical_distance))
              for k in range(num_stripes):
                    next_pos = i + k*2*vertical_distance
                    out_window[next_pos,:] = color
        elif (j==j_max-1):
             num_stripes = ceil((i_max-i)/(2*vertical_distance))
             for k in range(num_stripes):
                    next_pos = i + k*2*vertical_distance
                    out_window[next_pos,:] = color
    return out_window



