V = "aeiou"
plingua = ""

while True:# x frase
    p = input("Inserire la prima parola della frase da trasformare: ")
    for lettera in p:
        if lettera in V:
            plingua = plingua + lettera
        else:
            plingua = plingua + lettera + "o" + lettera
    print("La paola ", p, " diventa: ", plingua)

    continuo = input("Vuoi continuare con un altra parola? si o no ? ")
    if continuo == "no":
        break
