text = input("Entrez votre chaine de caractère:")
longueur = len(text)
c = 0
d = 0
while c < longueur:
    char = text[c]
    if (char == 'e'):
        print("Oh la lettre e")
        d += 1
    c +=1

print("Il y a",d,"e dans cette chaine de caractère")


