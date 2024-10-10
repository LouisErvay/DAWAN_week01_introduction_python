# Les types de base: int, bool, float, et str sont immuables

x = 10
print(id(x))
x = 11
print(id(x))

s = 'test'
s = s.upper()
print(s)

text = "ceci est une chaine"

print(f".upper() : {text.upper()}")
print(f".lower() : {text.lower()}")
print("ceci" in text)
print(f".startswith() : {text.startswith('ceci')}")
print(f".endswith() : {text.endswith('ceci')}")
print(f".strip() : {text.strip()}") # Suppréssion des espaces de début et de fin de chaine

print(f".rstrip() : {text.rstrip()}")
print(f".lstrip() : {text.lstrip()}")

print(f".replace() : {text.replace('e','a',2)}") # 2 représente le nombre de remplacements max

print(f".split() : {text.split()}") # Par défaut découpe sur les espaces

text2 = "mot1,mot2,mot3,mot4"

x = text2.split(',',2)
print(f".split(',') : {x}") # 2 -> nombres de coupures max, 2 coupures donc 3 éléments finaux

print(f".join() : {':'.join(x)}")