def increment_list(mylist):
    """This function adds 1 to each element of the list."""

    for i in range(len(mylist)):
        mylist[i] += 1

    return mylist


print(increment_list.__doc__)
print(increment_list([1, 2, 3]))


# the automatic documentation
# shows after you type """ and then press enter
def sample_function(paramx: int) -> int:
    """
    this sample function takes paramx is does this
    @type paramx: int
    @param paramx:
    @return: integer value by increasing the argument
    Example
    this is how you use my fuynction

    """
    paramx =+1
    return paramx

def demo_function(x,y):
    """

    @param x:
    @param y:
    @return:
    """
    return x+y
