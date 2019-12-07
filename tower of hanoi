def toh(n,A,B,C):
    if n>0:
        toh(n-1, A, C, B)   # transferring n-1 to intermediate disk B so last disk will be
                            # exposed for destination 
        print("Moving a disk from " + A + " to " + C)
        toh(n-1, B, A, C)  # when n-1 disk are on intermediate disk B and last one on destination C 
                           # # we will be transfering n-1-1 disk to intermediate A and last one to C via A

toh(3,"A","B","C")
