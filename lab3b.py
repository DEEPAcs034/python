from difflib import SequenceMatcher
str1 = input("Enter string 1:")
str2 = input("Enter string 2:")
sim = SequenceMatcher (None,str1,str2).ratio()
print("Similarity between strings\""+str1+"\"and\""+str2+"\"is:",sim)