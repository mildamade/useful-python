

# splits a list to sublists
def split_list_to_sublists(lst, subsize):
    n = int(len(lst) / subsize)
    return [lst[x*subsize:(x+1)*subsize] for x in range(0,n)]


# flatten list of lists
def flatten(lst):
    return [item for sublist in lst for item in sublist]