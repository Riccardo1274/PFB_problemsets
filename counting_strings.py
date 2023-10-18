#!/usr/bin/env python3

dna_string = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG' #get my string

#count the charachters in the string
print('the total length is\n', len(dna_string))
len_dna_string = len(dna_string)
#counting the different bases
nA = dna_string.count('A')
nC = dna_string.count('C')
nG = dna_string.count('G')
nT = dna_string.count('T')
print('the numbers of different bases are:\nnumber of A: ',nA,'\nnumber of C: ',nC,'\nnumber of G: ',nG,'\nnumber of T: ',nT)

#counting different bases if we have upper and lower letters
dna_string2 = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG'
dna_s2_up = dna_string2.upper()

nA2 = dna_s2_up.count('A')
nC2 = dna_s2_up.count('C')
nG2 = dna_s2_up.count('G')
nT2 = dna_s2_up.count('T')
print('the numbers of different bases are:\nnumber of A: ',nA2,'\nnumber of C: ',nC2,'\nnumber of G: ',nG2,'\nnumber of T: ',nT2)

#substituting all T with U
rna_string=dna_string.replace('T','U')
print(rna_string)
print('the number of T in RNA is\n', rna_string.count('T'))

#substituting all T with U but with the upper and lower seq
rna_s2_up=dna_s2_up.replace('T','U')
print(rna_s2_up)
print('the number of T in RNA is\n', rna_s2_up.count('T'))

#counting AT %
totAT = nA + nT
ATpercentage = (totAT/len_dna_string)*100
print('The total number of AT is\n' ,totAT, '\nThe percentage of AT is' ,ATpercentage,'%')
#counting GC %
totGC = nG + nC
GCpercentage = (totGC/len_dna_string)*100
print('The total number of GC is\n' ,totGC, '\nThe percentage of GC is' ,GCpercentage,'%')

#creating a substring from nt 100 to 200
dna_sub = dna_string[99:200]
print(dna_sub)

#counting the G in the substring
print(dna_sub.count('G'))

#counting the G in the substring of up and low
dna_sub2 = dna_string2[99:200]
print(dna_sub2)
dna_sub2up = dna_s2_up[99:200]
print(dna_sub2up)
print(dna_sub2up.count('G'))

#printing the reverse complement
a=dna_string.replace('A', 'a')
c=a.replace('C', 'c')
g=c.replace('G', 'g')
t=g.replace('T', 't') #creating a subsequence to substitute
T=t.replace('a', 'T')
G=T.replace('c', 'G')
C=G.replace('g', 'C')
dna_complement=C.replace('t', 'A') #created the complement
print(dna_string,'\n\n',dna_complement)
dna_rev_com=dna_complement[::-1]
print('\n',dna_rev_com)

