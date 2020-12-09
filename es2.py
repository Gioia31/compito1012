nparole = input("Scrivere una lista di parole separate da virgole (es. parola1, parola2,..).\n") 
listap = nparole.split(", ") #ad ogni , e spazio divide la lista per poi contare le lettere di ogni singola parola 
listalungp = []
for parola in listap:
    lunp = len(parola)
    listalungp.append(lunp)

print("La lunghezza delle parole è di ", listalungp)
