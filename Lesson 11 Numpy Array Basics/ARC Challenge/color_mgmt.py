# create custom color mapping
import matplotlib.colors as mcolor
import matplotlib.pyplot as plt
import copy
colors = ['black', 'green', 'yellow','red','blue']
bounding_color = "green"
surround_color = "yellow"
# blue for showing parents
# red for current cell being processed
num_to_color_map = {0:'black', 3: 'green', 4: 'yellow', 5:'red', 6:'blue'}
color_to_num_map = {'black':0, 'green':3, 'yellow':4,'red':5, 'blue':6}

bounds = [0, 3, 4, 5, 6, 7]  # The bounds for our colormap (use 5 to include the maximum value)
cmap = mcolor.ListedColormap(colors)
norm = mcolor.BoundaryNorm(bounds, cmap.N)

def visualize_array(array_obj, i=-1, j=-1, parent_cells=[], custom_colormap=None):
    # make a copy to visualize search
    local_arr = copy.deepcopy(array_obj)
    if (i>0) and (j>0):
        local_arr[i,j] = color_to_num_map['red']
    for n,k in parent_cells:
        local_arr[n,k] = color_to_num_map['blue']
    if custom_colormap is not None:
        c=plt.pcolor(local_arr,cmap=custom_colormap)
    else:
        c=plt.pcolor(local_arr,cmap=cmap, norm=norm, shading='auto')
    plt.colorbar(c)
    plt.show()