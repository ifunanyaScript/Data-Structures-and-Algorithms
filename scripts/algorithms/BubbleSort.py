# Iterative bubble sort.
def bubble_sortI(array):
    length = len(array)
    
    # Loop through the array.
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break


# Recursive bubble sort.
class RecursiveBubbleSort:
    def __init__(self, array):
        self.array = array
 
    def bubble_sortR(self, len_array):
        # Condition for recursion.
        if (len_array == 0 or len_array == 1):
            return
        
        # Loop through the array.
        for i in range(len_array - 1):
            if self.array[i] < self.array[i+1]:
                self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
        
        # Recursive operation.
        self.bubble_sortR(len_array - 1)
        
        # Return sorted array.
        return self.array
    
    
    def print_array(self, array):
        # Condition for recursion.
        if len(array) == 0:
            return
        item = array.pop()
        print(item, end=", ")
        self.print_array(array)

# Sorting operation.
def sort(array):
    length = len(array)
    algo = RecursiveBubbleSort(array)
    sorted_array = algo.bubble_sortR(length)
    algo.print_array(sorted_array)


if __name__ == "__main__":
    print("This is a demo of a bubble sort algorithm, from ifunanyaScript.")
    print("_" * 63, "\n")
    print("Iterative bubble sort-->")
    print("\nUnsorted array:")
    array = [4, 1, 66, 8, 2, 39, 90, 6, 450, 32]
    print(array)
    print("_" * 36)
    print("\nSorted array:")
    bubble_sortI(array)
    print(array)
    print("\n")
    print("_"*36)
    
    print("\nRecursive bubble sort-->")
    print("\nUnsorted array:")
    array = [4, 1, 66, 8, 2, 39, 90, 6, 450, 32]
    print(array)
    print("_" * 36)
    print("\nSorted array:")
    sort(array)


# ifunanyaScript