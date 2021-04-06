

def CyclicSort(arr):

    freq_list = [0]*100
    result = []
    # appends the number in the at its index
    for item in arr:
        freq_list[item] += 1


    for index in range(len(freq_list)): # get the number at particular index
        for freq in range(freq_list[index]): # append the index number as many times it is present in the freqency list
            result.append(index)

    return print(result)

CyclicSort([98, 66, 98, 56, 29, 54, 1, 41, 4, 48, 69, 65, 30, 3, 83, 59, 87, 33, 2, 19, 36, 19, 61, 36, 21, 40, 22, 88, 71, 3])



