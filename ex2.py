# coding: utf-8
DNAseq='ACGT'*3+'TTATT'*5
for i in range(len(DNAseq)):
        print DNAseq[i:len(DNAseq)]
        i+=1
    
for i in range(len(DNAseq)-2):
    print DNAseq[0+i:3+i]
    i+=1
    
UniEle=[]
for i in range(len(DNAseq)-2):
    if DNAseq[0+i:3+i] in UniEle:
        UniEle=UniEle
        i+=1
    else:
        UniEle.append(DNAseq[0+i:3+i])
        i+=1
        
UniEle
