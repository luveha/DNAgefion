import string
#Defines
DNAcombinations = ['UUU','UUC','UUA','UUG','CUU','CUC','CUA','CUG','AUU','AUC', 'AUA','AUG','GUU','GUC','GUA','GUG','UCU','UCC','UCA','UCG','CCU','CCC','CCA','CCG','ACU','ACC','ACA','ACG','GCU','GCC','GCA','GCG','UAU','UAC','UAA','UAG','CAU','CAC','CAA','CAG','AAU','AAC','AAA','AAG','GAU','GAC','GAA','GAG','UGU','UGC','UGA','UGG','CGU','CGC','CGA','CGG','AGU','AGC','AGA','AGG','GGU','GGC','GGA','GGG']
AminoAcids = ['Phe','Phe','Leu','Leu','Leu','Leu','Leu','Leu','Ile','Ile','Ile','Met','Val','Val','Val','Val','Ser','Ser','Ser','Ser','Pro','Pro','Pro','Pro','Thr','Thr','Thr','Thr','Ala','Ala','Ala','Ala','Tyr','Tyr','STOP','STOP','His','His','Gln','Gln','Asn','Asn','Lys','Lys','Asp','Asp','Glu','Glu','Cys','Cys','STOP','Trp','Arg','Arg','Arg','Arg','Ser','Ser','Arg','Arg','Gly','Gly','Gly','Gly']
AllowedLetters = set('ATCG ')
ErrorText = 'Der er indsat et/flere bogstav som ikke er enten A, T, C eller G'
cursorVal = 1
NiceDude = 'D:\Python\DNAgefion-master\DNAgefion-master\gefipngon.png'
