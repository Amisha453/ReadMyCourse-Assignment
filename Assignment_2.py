#creating the list

list_example=[]
print(list_example)
names=["Amisha","Ankita"]

acc_ids=["AYC101","AYC105","AYC108"]

gc_percentages=[40.4,76.8,88]

print(names,acc_ids,gc_percentages)


#nested lists
records=[1,2,"Amisha","TAGAA",35.4,[1,2,3]]
print(records)
#creating the list

list_example=[]
print(list_example)
names=["Amisha","Ankita"]

acc_ids=["AYC101","AYC102","AYC103"]

gc_percentages=[30.4,56.8,98]

print(names,acc_ids,gc_percentages)


#nested lists
records=[1,2,"Amisha","TAGAA",35.4,[1,2,3]]
print(records)
#indexing and slicing
#          -3       -2      -1
acc_ids=["AYC101","AYC102","AYC103"]
#          0        1        2
print(acc_ids[0])
print(acc_ids[2])
print(acc_ids[-1])

print(acc_ids[1:3])
print(acc_ids[1:3][0])
print("ATGCATGGGGCC")
"""
This program was created on 28-9-2021
"""
print("ATGCATGGGGCC")
print("Message 1","Message 2")
print("ATGATAGATA","ATGATAGATAT","ATGCTAGTAA")
print("ATGATAG","ATGATAG",sep="*")
print("ATGATAG","ATGATAG","ATGATAG",sep="*")
print(34.5)
print(type(34.5))
print(type(-34.5))
print(1)
print(type(1))
print(-2)
print(type(-2))
print("ATGCTAG")
print("AUGC")
print(type("AUGC"))
print(type("ATGCTAG"))
print(type("34.5"))
print("ATAGTAAA")
print(len("ATAGTAAA"))
seq="ATGATAGATGATAGATAA"
#    0123456789
print(seq)
#indexing == name_of_seq[index]
print(seq[2])
print(seq[5])
print("ATGCCCTAG")
print(seq[3])
print(seq[1:5])
print(seq[2:6])
dna_seq="ATGATAGTAGTAGAGATA" 
length=len(dna_seq)
print(dna_seq[:int(length/2)])
print(dna_seq[int(length/2):])
dna_seq="ATGATAGTAGTAGAGATA" 
length=len(dna_seq)
print(seq[:int(length/2)])
seq="AATGATGATaatTAG"
# upper()==>convert sequences to upper case
print(seq.upper())
# lower()==>convert sequences to lower case
print(seq.lower())
# count() ==>gives you the count of chars
seq="ATGCC"
print(seq.count("A"))
print(seq.count("C"))
# find()==>to find first occurrence of character
# replace()==> to replace a character with any specific character
# [::-1]==>to reverse the sequence
seq="ATGCATGCCCCGG"
print(seq.find("A"))
dna_seq="atgcatgcaattggcc"
res_enz_site="atgc"
print(dna_seq.find(res_enz_site))
# [::-1]==>to reverse the sequence

dna_seq="atgc"
print(dna_seq[::-1])
dna_seq='ATGCATGC'
mrna_seq=dna_seq.replace('T','U')
mrna_seq
#lowercase code
dna_seq='ATGCATGC'
dna_seq.lower()