


def CountSort(arr):

    freq_list, result = [0]*100, []

    # placing item placed in their respective index and the freq of the number is increased
    for item in arr:
        # initial the the freq of item is zero
        freq_list[item] = freq_list[item] + 1
    # in this case the index of freq list is always arranged sorted


    # the below loop is used to get each item(sorted index) from freq. list
    for index in range(len(freq_list)):
        # the below loop will iterate as many times the index is present
        for freq in range(freq_list[index]):
            # if freq of the number is zero it will not add the number
            # if number is present it will append as many times into result
            result.append(index)
    
    return print(result)
CountSort([98, 66, 98, 56, 29, 54, 1, 41, 4, 48, 69, 65, 30, 3, 83, 59, 87, 33, 2, 19, 36, 19, 61, 36, 21, 40, 22, 88, 71, 3])