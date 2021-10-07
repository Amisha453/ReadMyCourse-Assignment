#1.Write a program to calculate the length of DNA Sequence in python. Take the sequence from user.
sequence=input("Please enter the sequence: ")
print("The length of the sequnece=",len(sequence))

#Write  a program to calculate the GC percentage of DNA sequence. Take the sequence from the user.
seq = input("Please enter the Sequence:")
total = len(seq)
G = seq.count("G")
C = seq.count("C")
GC_total = G+C
GC_content = GC_total/float(total)
print(GC_content)