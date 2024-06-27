# Problem 1
def remove_duplicates(array):
    if not array:
        return 0
    
    write_index = 1
    for read_index in range(1, len(array)):
        if array[read_index] != array[read_index - 1]:
            array[write_index] = array[read_index]
            write_index += 1
    
    return write_index

if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9]))  # 6
    print(remove_duplicates([2, 2, 2, 11]))          # 2
    print(remove_duplicates([2, 2, 2, 11]))          # 2
    print(remove_duplicates([1, 2, 3, 11, 11]))      # 4
