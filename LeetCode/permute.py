def permute(unproc, result= [], proc = ""):



    if unproc == "":
        result.append(proc)
        return 


    for index, item in enumerate(unproc):
        permute(unproc[:index] + unproc[index + 1:], result, proc + item)


    return print(result)

permute("12")