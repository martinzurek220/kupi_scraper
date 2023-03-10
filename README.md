# kupi_scraper
Jeden z mých prvních scraper programů. Jedná se scraper portálu https://www.kupi.cz/. Program načte z textového souboru url adresy produktů 
na kupi a poté o těchto produktech stáhne informaci o prodejci, ceně, množství, trvání slevy a pošle je do emailu. 

Program je v původním stavu a není aktualizovaný.

Použité knihovny:
- Pro parsování dat je použita knihovna <b>Beautifulsoup</b>

## Příklad výstupu
Zbozi: Máslo Jihočeské Madeta, Obchod: BILLA, Cena: 49,90 Kč, Mnozstvi: 250 g, Trvani: v so 11. 3. <br>
Zbozi: Máslo Jihočeské Madeta, Obchod: Albert, Cena: 49,90 Kč, Mnozstvi: 250 g, Trvani: platí do úterý 14. 3. <br>
Zbozi: Přírodní voda Magnesia, Obchod: Albert, Cena: 14,90 Kč, Mnozstvi: 1.5 l, Trvani: platí do úterý 14. 3. <br>
Zbozi: Přírodní voda Magnesia, Obchod: PennyMarket, Cena: 14,90 Kč, Mnozstvi: 1.5 l, Trvani: platí do středy 15. 3. <br>
Zbozi: Přírodní voda Magnesia, Obchod: JIP CCCash&Carry, Cena: 14,90 Kč, Mnozstvi: 1.5 l, Trvani: platí do pondělí 13. 3. <br>

## Další postup ve vývoji projektu
- Rozdělit kód do funkcí
- Nastavit, aby se do mailu posílaly jen produkty, jehož cena je pod předem nastavenou hranicí
