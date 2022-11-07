# Import time_it for time comprison.
from utils import timely


@timely
def linear_search(array, search_key):
    for index, element in enumerate(array):
        if element == search_key:
            return index
    return -1

# Iterative binary Seach.
@timely
def binary_searchI(array, search_key):
    # Minimum index.
    mini = 0
    # Maximum index.
    maxi = len(array) - 1
    
    while mini <= maxi:
        # Middle index.
        midi = (mini+maxi)//2
        mid_num = array[midi]
        
        if mid_num == search_key:
            return midi
        
        # Upper half
        if mid_num < search_key:
            mini = midi + 1
        # Lower half
        else:
            maxi = midi - 1
            
    return -1

# Recursive binary search.
def binary_searchR(array, search_key, mini, maxi):
    if maxi < mini:
        return -1
    
    midi = (mini+maxi)//2
    if midi >= len(array) or midi < 0:
        return -1
    
    mid_num = array[midi]
        
    if mid_num == search_key:
        return midi

    # Lower half
    if mid_num > search_key:
        maxi = midi - 1
    # Upper half
    else:
        mini = midi + 1
    
    return binary_searchR(array, search_key, mini, maxi)


# This function finds all the indices of a search key.
def find_indices(array, search_key):
    index = binary_searchI(array, search_key)
    indices = [index]
    
    # Lower half.
    i = index - 1
    while i >= 0:
        if array[i] == search_key:
            indices.append(i)
        else:
            break
        i = i - 1
    
    i = index + 1
    
    # Upper half.
    while i < len(array):
        if array[i] == search_key:
            indices.append(i)
        else:
            break
        i = i + 1
    
    return sorted(indices)

# Execution.
if __name__ == "__main__":
    print("This is a demo of comparison between linear search and binary search, from ifunanyaScript.")
    print("_" * 90)
    array = [*range(1, 200000000)]
    search_key = 50056
    # Linear searching
    index = linear_search(array, search_key)
    print(f"Search key found at index {index} using linear search.")
    print("_" * 51)
    print("\n")
    index = binary_searchI(array, search_key)
    print(f"Search key found at index {index} using binary search.")
    print("_" * 54)
    print("\n")
    index = binary_searchR(array, search_key, mini=0, maxi=(len(array)-1))
    print(f"Search key found at index {index} using Recursive binary search.")
    print("_" * 62)
    print("\n")
    array[50053] = 50056
    array[50054] = 50056
    array[50056] = 50056
    array[50057] = 50056
    print(f"Indices where {search_key} can be found: {find_indices(array, search_key)}")


# ifunanyaScript