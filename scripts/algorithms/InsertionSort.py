# Insertion Sort.
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key

# Running the sorting program...
if __name__ == "__main__":
    print("This is an Insertion sort demo, from ifunanyaScript")
    print("_"*46)
    arrays = [
        [32, 4, 1, 300, 32, 9, 45, 78, 15, 45, 43, 97, 17],
        [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],
        [450, 409, 367, 301, 275, 101, 27],
        [123456789],
        [],
        [0.4, 0.25, 0.075, 0.9, 0.75]
    ]
    for array in arrays:
        print(f"\nUnsorted array: {array}")
        insertion_sort(array)
        print(f"Sorted array: {array}")
        print("_" * 66)

# ifunanyaScript