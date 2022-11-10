# Importing time to spice the program.
import time

# Hoare's Partitioning technique.
def partitionH(array, start, end):
    pivot_index = start
    pivot = array[pivot_index]
    
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start < end:
            array[start], array[end] = array[end], array[start]
    
    array[pivot_index], array[end] = array[end], array[pivot_index]
    
    # return partition index.
    return end
    
# `quick_sortH` recursively calls `partitionH`, hence the sorting.
def quick_sortH(array, start, end):
    if start < end:
        pi = partitionH(array, start, end)
        # Left partition.
        quick_sortH(array, start, pi-1)
        # Right partition.
        quick_sortH(array, pi+1, end)



# Lomuto's Partitioning technique.
def partitionL(array, start, end):
    pivot = array[end]
    p_index = start
    
    
    for i in range(start, end):
        if array[i] <= pivot:
            if i != p_index:
                array[i], array[p_index] = array[p_index], array[i]
            p_index += 1
    
    array[p_index], array[end] = array[end], array[p_index]
    
    return p_index

# `quick_sortL` recursively calls `partitionH`, hence the sorting.
def quick_sortL(array, start, end):
    if start < end:
        pi = partitionL(array, start, end)
        # Left partition.
        quick_sortL(array, start, pi-1)
        # Right partition.
        quick_sortL(array, pi+1, end)


# Running the sorting program...
if __name__ == "__main__":
    print("This is a Quick Sort demo, from ifunanyaScript")
    print("_"*46)
    time.sleep(1)
    arrays = [
        [32, 4, 1, 300, 32, 9, 45, 78, 15, 45, 43, 97, 17],
        [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],
        [450, 409, 367, 301, 275, 101, 27],
        [123456789],
        [],
        [0.4, 0.25, 0.075, 0.9, 0.75]
    ]
    print("\nHoare's Partition...")
    time.sleep(1)
    for array in arrays:
        print(f"\nUnsorted array: {array}")
        quick_sortH(array, 0, len(array)-1)
        print(f"Sorted array: {array}")
        print("_" * 66)
        time.sleep(1)

    print("\n\nLomuto's Partition...")
    time.sleep(1)
    for array in arrays:
        print(f"\nUnsorted array: {array}")
        quick_sortL(array, 0, len(array)-1)
        print(f"Sorted array: {array}")
        print("_" * 66)
        time.sleep(1)


# ifunanyaScript