# if else toussa toussa

# Ternaire
age = 10
status = "mineure" if age < 18 else "majeure"

# match/case (switch/case de java)
note = input("donne un chiffre")

match note:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case other:
        print(note)