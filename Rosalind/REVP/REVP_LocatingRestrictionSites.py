# REVP
# having issues with this
# it's almost working !!

from Bio.Seq import Seq
s = "TCAATGCATGCGGGTCTATATGCAT"
seq = Seq(s)

def get_reverse_comp(seq):
    return(str(seq.reverse_complement()))

def get_Palindrome(s):
    return s[::-1]

def isReverseComplement(s):
    seq = Seq(s)
    rev = str(seq.reverse_complement())
#    return rev[::-1]
    return rev

 for x in range(0, len(s)):
    for window_size in range(4, 12):
        if len(s) <= window_size:
            print("")
    for location in range(len(s)):
        window_slice = (s[location:location+window_size])
#        if window_slice == get_Palindrome(window_slice):
        if(window_slice == isReverseComplement(window_slice)):
            print(window_slice)
            print(isReverseComplement(window_slice))
            print(location)