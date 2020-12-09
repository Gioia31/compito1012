print("Il seguente programma riconosce se la parola fornita è un pallindromo.")

pfornita = input("Inserire la parola: ")
pgirata = pfornita[::-1] #gira la stringa

if pfornita == pgirata:
    print(pfornita," è un pallindromo.")
else:
    print(pfornita," non è un pallindromo.")
