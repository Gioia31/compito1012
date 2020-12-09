import math
fgeom = input("Quadrato, rettangolo, triangolo, cerchio\nDi quale di queste figure geometriche vuoi conoscere l'area? ")

if fgeom == "quadrato":
    l = float(input("Inserire il lato del quadrato: "))
    areaq = l * l
    print("L'area del quadrato è ", areaq)

elif fgeom == "rettangolo":
    b = float(input("Inserire la base del rettangolo: "))
    h = float(input("Inserire l'altezza del rettangolo: "))
    arear = b * h
    print("L'area del rettangolo è ", arear)

elif fgeom == "triangolo":
    b = float(input("Inserire la base del triangolo: "))
    h = float(input("Inserire l'altezza del triangolo: "))
    areat= (b * h)/2
    print("L'area del triangolo è ", areat)

elif fgeom == "cerchio":
    r = float(input("Inserire il raggio del cerchio: "))
    areac = (r * r)* math.pi
    print("L'area del cerchio è ", areac)

else:
    print("La formula dell'area di questa figura non è disponibile.")