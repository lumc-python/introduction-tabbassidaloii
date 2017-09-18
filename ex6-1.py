# coding: utf-8
def UniStr(input,k_mer=3):
    output=[]
    for i in range(len(input)-(k_mer-1)):
        if input[0+i:k_mer+i] in output:
            output=output
            i+=1
        else:
            output.append(input[0+i:k_mer+i])
            i+=1
    return output
