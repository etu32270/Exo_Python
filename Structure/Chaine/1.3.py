text = input("Entrez une chaine de caractere: ")
a = 0
ntext=""
while a < len(text):
    ntext=ntext+(text[a]+"*")
    a +=1

print(ntext)