import re

# regex groups

text = """Kody pocztowe poszczególnych krajów są poprzedzone narodowym prefiksem składającym się z 1- lub 2-literowego oznaczenia kraju (tzw. kod kraju). W tej roli występują samochodowe oznaczenia przynależności – początkowo eksponowane na eliptycznej tabliczce, a obecnie w Unii Europejskiej włączone do tablic rejestracyjnych. Brak jest uregulowań w tej sprawie i obecnie obserwuje się tendencję do używania kodów dwuliterowych zgodnych z normą ISO 3166-1 alfa-2 (i jednocześnie analogicznych do oznaczeń domen internetowych najwyższego poziomu — np. zamiast H – HU oznacza Węgry).[potrzebny przypis]

W tym wypadku kod zwykło się podawać bez dywizu. Dla przykładu:

PL-00001 (zamiast 00-001 Warszawa)
A-1130 – przykładowy kod pocztowy dla Wiednia w Austrii
Nie jest to standard zatwierdzony przez Światowy Związek Pocztowy. /Wikipedia"""

postalCodeRegex = re.compile(r"(\d\d)-(\d\d\d)")
mo = postalCodeRegex.search(text)
print("Mo.group: " + str(mo.group()))
print("Mo.group(1): " + str(mo.group(1)))
print("Mo.group(2): " + str(mo.group(2)))

# Output to the console:
# Mo.group: 00-001
# Mo.group(1): 00
# Mo.group(2): 001



