# Pour manipuler / créer des dates, il y a trois classes
import time
from datetime import date, datetime, timedelta

# Création de date:
today = date.today()
print(today)

before = date(2018,5,28)
print(before)

# Création de datetime:
now = datetime.now()
print(now)

other = datetime(2017,8,12,14,32,56,52665)
print(other)

# doc strftime -> https://strftime.org/
print(other.strftime('%B'))

# Création de timedelta
interval = timedelta(days=4)
print(today+interval)

max_time = now + timedelta(seconds=10)
while datetime.now() <= max_time:
    print(datetime.now())
    time.sleep(1)

# L'heure Unix ou l'heure Posix (aussi appelée Unix Timestamp)
# est une mesure du temps fondée sur le nombre de secondes depuis le 01 Janvier 1970 00:00:00
# Le module time de Python permet de gérer l'horodatage de façon Unix,
# affiche un nombre à virgule sans aucunne mention de jours / mois / année

# On utilise le module time
import time