# coding: utf-8
def CountStr(input,k_mer=3):
    """Compute k-mer frequencies"""
    output={}
    for i in range(len(input)-(k_mer-1)):
        string=input[0+i:k_mer+i]
        count=input.count(string)
        output[string]=count
        i+=1
    return output
