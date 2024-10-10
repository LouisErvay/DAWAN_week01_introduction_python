# 3 types d'erreurs possibles :

# - Erreurs de syntaxes ( de compilations): Elles sont détectées automatiquement par l'IDE
# - Exceptions: se sont des erreurs qui provoquent l'arrêt de l'application
# - Code fonctionnel, mais qui renvoie un résultat inattendu -> débuggage -> print("ICI")

# Pour éviter l'arret de l'application, on doit gérer l'exception
# Pour ce faire, on utilise un try-except

# Il existe plusieurs types d'exceptions possibles. Chacune d'elles porte le nom de l'erreur qu'elle génère.
# Il existe un type générique d'exception (Exception) qui inclus toutes les exceptions.

try:
    print(10/0)
    x = "lol" + 5

except ZeroDivisionError:
    print("DEVIDE BY 0 IS FORBIDDEN")
except TypeError:
    print("une erreur de type")

print("Ez les erreurs perso je les vois pas")


# Réceupérer l'exception
try:
    print(10/0)

except Exception as e:
    print(e)

else:
    # Exécuté si il n'y a pas eu d'erreurs dans le try
    pass

finally:
    # Exécuté dans 100% des cas
    pass