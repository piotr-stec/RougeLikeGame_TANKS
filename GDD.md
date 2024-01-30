# ROUGELIKE GAME - TANKS
1. Ogólny zamysł gry
- TANKS jest to gra przedstawiająca interesujący świat czołgów zmagających się pomiędzy sobą. Gracz będzie kontrolował czołg, rozwijał go oraz podejmował wyzwania eksplorując losowo generowany świat pełen wrogich jednostek i trudności.

2. Rozgrywka 
- Celem gry jest przetrwanie jak największej ilości poziomów oraz pokonanie najtrudniejszych przeciwników na ostatnim poziomie. Bohater będzie musiał odpowiednio zarządzać zasobami, aby wystarczyły mu na całą rozgrywke.
- Gracze będą mogli zbierać przedmioty znajdujące się na mapie takie jak amunicja oraz zestawy naprawcze. Progresja oraz dobre zarządzanie zasobami będzie ważnym elementem rozgrywki, zachęcając graczy do eksploracji i rozwoju.
- Po utracie wszystkich punktów wytrzymałości nie ma możliwości naprawy czołgu. Gracz traci wszystkie osiągniecią zdobyte do tego momentu i zaczyna grę od początku.

- Aby przejść do następnego poziomu okopów należy zniszczyć wszystkich przeciwników - następnie gracz ma możliwość dalszego zbierania przedmiotów na mapie.
- Czołgi mają różne wartości życia oraz ilość zadawanych obrażeń. 
- Po przejściu do następnego poziomu gracz automatycznie dostaje bonus w postaci 30% dodatkowego hp które mu pozostało. Średnie obrażenia zostają liniowo zwiększane tzn. DMG + LVL*10.
- W następnych poziomach zwiększa się wartość itemów - Zestaw naprawczy dodaje więcej punktów życia oraz pociski występują w większej ilości

- W walce liczy się przedewszystkim średnia ilość zadawanych obrażeń przez oponenta bądź gracza. Konkretna wartość zadanych obrażeń waha się od +25% do -25% i jest generowana losowo. Atak wykonywany jest w najbliższą istote i zadaje losową wartość obrażeń

- Gracz posiada ekwipunek zawierający informacje dotyczące przechowywanej amunicji. Są dwa typy pocisków: GoldAmmo - zadaje 15% więcej obrażeń niż DefaultAmmo. Początkowo postać posiada 10 pocisków standardowych oraz 5 ulepszonych. W czasie rozgrywki musi zdobywać większe zasoby amynicji.

3. Przeciwnicy
- MS1 posiada 100 pkt hp oraz średni dmg na poziomie 25, zasięg: 3 kratki - nie stanowi większego zagrożenia dla gracza nawet na początkowym poziomie
- T28 posiada 200 pkt hp oraz średni dmg na poziomie 45, zasięg: 4 kratki - nie stanowi większego zagrożenia dla gracza lecz może już wyrządzić mu szkodę
- KV85 posiada 300 pkt hp oraz średni dmg na poziomie 60, zasięg: 5 kratek - jest z graczem w początkowym stanie równy 1:1 i szansa na jego pokonanie to 50%
- IS3 posiada 400 pkt hp oraz średni dmg na poziomie 80, zasięg: 6 kratek - jest ogromnym zagrożeniem dla gracza ale jest szansa na pokonanie
- OBJ277 posiada 800 pkt hp oraz średni dmg na poziomie 120, zasięg: 7 kratek - początkowy gracz nie ma z nim żadnych szans


4. Sterowanie
- Gracz porusza się za pomocą W A S D ctrl
- ENTER słóży do ataku przeciwnika gdy jest w zasięgu
- C podniesienie przedmiotu z mapy
- I menu gry oraz dostęp do większej informacji na temat rozgrywki
- N przejście do następnego poziomu po pojawieniu się komunikatu, że jest to możliwe

5. Świat
- Gra odbywa się w losowo generowanych okopach, w których będą poruszać się czołgi oraz znajdować przeciwnicy o różnej trudności
- Grafika przedstawiana jest za pomocą kodów ASCII 
