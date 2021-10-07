#1.Write a program to calculate the length of DNA Sequence in python. Take the sequence from user.
sequence=input("Please enter the sequence: ")
print("The length of the sequnece=",len(sequence))

#2.Write  a program to calculate the GC percentage of DNA sequence. Take the sequence from the user.
seq = input("Please enter the Sequence:")
total = len(seq)
G = seq.count("G")
C = seq.count("C")
GC_total = G+C
GC_content = GC_total/float(total)
print(GC_content)

#3. program to mutate a sequence taken from user. Accept sequence as a input from the user. Take position and mutated base as argument.
seq = input("Please enter the Sequence:")
mutated_seq=seq[:3]+"A"+seq[4:]
print(seq)
print(mutated_seq)

#4.Write a program to slice the sequence in two halves. Print the result. Take the sequence from the user
DNA_seq = input("Please enter the Sequence:")
DNA_seq_first= DNA_seq(:len(DNA_seq)/2) 
print(DNA_seq_first)

                        