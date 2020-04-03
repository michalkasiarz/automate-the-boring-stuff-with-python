import re

# using pipeline

text = """
Początkowo Batman używał broni palnej, a nawet zabijał swoich oponentów. Dopiero, kiedy w 1940 roku redaktorem komiksów o przygodach tej postaci został Whitney Ellsworth, Batman zaczął posługiwać się kodeksem moralnym, który zabraniał mu zabijać i korzystać ze śmiercionośnej broni[12][13]. Odtąd, aby móc prowadzić swoją krucjatę ze zbrodnią, Batman zaczął posługiwać się wyłącznie gadżetami i wysoce zaawansowaną technologią. Z lubością, nazywając swoje wynalazki, dodaje przedrostek bat- (ang. nietoperz), np. batlina, batmobil.

Wyposażenie
Kostium Batmana (ang. Batsuit) – kostium jaki nosi Bruce Wayne ma przede wszystkim za zadanie skrywać jego tożsamość i kreować mroczny wizerunek, ale także posiada wiele innych praktycznych zastosowań. Zarówno w komiksie, jak w różnego rodzaju adaptacjach jego kostium się rozwijał. Obecnie w komiksach składa się m.in. z kamizelki kuloodpornej z kevlaru, peleryny, mogącej posłużyć jako lotnia i maski z wmontowanym noktowizorem i termowizorem. Jego maska pełni również rolę hełmofonu, dzięki któremu może nawiązać kontakt ze sprzymierzeńcami.
Pas z wyposażeniem (ang. Utility Belt) – pełen schowków do trzymania poręcznych sprzętów. Jeśli wróg zdoła pozbawić Batmana pasa, odczuwalnie obniża jego wartość bojową. Zawiera m.in. batrangi, małe urządzenia naprowadzające (przypinane magnesem do pojazdów wrogów), pluskwy (urządzenia służące do podsłuchu), wytrychy, kajdanki, piłę oscylacyjną, laser do cięcia, granaty gazowe i dymne, maskę przeciwgazową, noktowizor (chyba że w danej produkcji jest częścią kostiumu) oraz przedmioty przydatne do zbierania, zabezpieczenia i badania śladów na miejscu zbrodni. W niektórych historiach Batman przetrzymuje tam pierścień z kryptonitu, na wypadek gdyby przyszło mu zmierzyć się z Supermanem lub innymi przedstawicielami jego niemal doszczętnie wymarłej rasy (np. Batman: Hush[14]). Warto nadmienić, że takie same pasy noszą powiązani z Batmanem Robin i Batgirl.
Batrangi (ang. Batrangs) – są to bumerangi w kształcie mniej lub bardziej podobnym do logo Batmana. Często z ostrymi krawędziami. Mają wiele zastosowań: wytrącanie broni lub innych przedmiotów z ręki wroga, niszczenia jego sprzętu, spowodowanie że coś nad jego głową spadnie etc. Batman rzuca nimi z wielką celnością, nawet na znaczące odległości. Mogą zawierać niewielkie ładunki wybuchowe. Czasami dołączony jest do nich sznur, który pozwala obezwładnić uciekającego wroga albo wspiąć się (batarang pełni rolę kotwicy). Niekiedy wzorowane są na japońskim shuriken.
Batbolas – rodzaj bolas, służących do obezwładnienia przeciwnika.
Batlina lub wyrzutnia kotwicy do wspinaczki (ang. Batrope lub Grapple gun) – urządzenie do wspinaczki, działające jak działo harpunnicze. Zakończona kotwicą lub grotem, wystrzeliwana małym ładunkiem wybuchowym. Pozwala szybko zmieniać miejsce przebywania, wspinać się na dachy, przeskakiwać przez przeszkody etc.
Pojazdy
Batmobil – najczęściej wykorzystywany pojazd. Początkowo w komiksach Batman jeździł zwykłymi samochodami. Batmobil ma małą kabinę, wielką maskę, charakterystyczny jest silnik rakietowy z tyłu. Pojazd jest opancerzony, wyposażony w komputer sterowany głosem.
Batcycle – motocykl.
Batplane/Batwing – samolot lub inny pojazd latający.
Batboat – łódź. / Batman - Wikipedia
"""

batRegex = re.compile(r"Bat(mobile|copter|rag|bolas|lina|plane|wing|suit|cycle|boat)")
mo = batRegex.search(text)
print(mo.group())
