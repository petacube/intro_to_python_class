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

    @type paramx: int
    @param paramx:
    @return:
    """
    paramx =+1
    return paramx
