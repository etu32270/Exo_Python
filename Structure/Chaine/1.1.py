text = input("Entrez votre chaine de caractere: ")
longueur = len(text)
c = 0
while c < longueur:
    char = text[c]
    if(char == "e"):
        print("OK")
    c += 1