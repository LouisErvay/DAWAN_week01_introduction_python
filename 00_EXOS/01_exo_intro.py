# 1) Lire un nombre saisi au terminal. Afficher si le nombre est pair
# 2) Lire un mot saisi dans le terminal. Afficher si la lettre E en fait partit

number = int(input("donne un nombre: "))
print("Nombre pair" if number%2 == 0 else "nombre impair")

mot = input("donne un mot: ")
print("Y'a un E !" if "e" in mot else "Y'a pas de E !")