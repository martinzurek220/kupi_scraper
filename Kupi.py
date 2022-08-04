# Tipy pro rozsireni projektu:
#  - Nazev txt bude ve formatu datum a cas
#  - Do mailu se poslou jen slevy, ktere jsou zajimave (cena do XX Kc) + nastavit hranici

import requests
from bs4 import BeautifulSoup
import os

# Vsechno jsou to knihovny na emaily
from email.mime.text import MIMEText
import smtplib
import sys


os.system("cls")

# URL = "https://www.kupi.cz/…son"
# URL = "https://www.kupi.cz/…eta"
# URL = "https://www.kupi.cz/…ico"


# Nacteni textoveho souboru
soubor_file = open("kupi_adresy.txt", "r")
# Pri pouziti soubor_statistiky = soubor_file.read() se do listu ulozi adresa
# po pismenkach a ne cely radek
# soubor_statistiky = soubor_file.read()
# soubor_file.close()

adresy_kupi = []

# Ulozi adresy ze souboru do listu a odstrani nadbytecne znaky
for URL_line in soubor_file:
    # print(URL_line)
    adresy_kupi.append(URL_line.strip())
soubor_file.close()


muj_slovnik = {}
idx = 0

# Nacteni do slovniku
for URL_line in adresy_kupi:

    print(URL_line)

    odpoved = requests.get(URL_line)

    bsObj = BeautifulSoup(odpoved.text, "html.parser")

    # print(bsObj.find("h1", {"class": "product_detail_headline"}).text.strip())
    zbozi = bsObj.find("h1", {"class": "product_detail_headline"}).text.strip()

    # Pokud je zbozi ve sleve
    if bsObj.find_all("tr", {"class": "discount_row"}) != []:
        # Projde vsechny tagy "tr" - jeden tag "tr" = jeden obchod
        for x in bsObj.find_all("tr", {"class": "discount_row"}):

            muj_slovnik['Polozka_' + str(idx)] = {}

            muj_slovnik["Polozka_" + str(idx)]["Zbozi"] = zbozi

            # Vypise nazev obchodu
            # Kdyz je nazev obchodu slozen ze dvou slov napr. Tesco hypermarket, tak druhe slovo vlozi na novy radek
            # a mezi tato slova se vlozi hodne mezer napr. Tesco                 Hypermarket a je potreba je odstranit
            # proto .replace(" ", "") a .replace("\n", " ") -> Tesco hypermarket
            print(x.find("span", {"class": "discounts_shop_name"}).text.strip().replace(" ", "").replace("\n", " "))
            muj_slovnik["Polozka_" + str(idx)]["Obchod"] = x.find("span", {"class": "discounts_shop_name"}).text.strip().replace(" ", "").replace("\n", " ")

            # Vypise cenu
            print(x.find("strong", {"class": "discount_price_value"}).text.strip())
            muj_slovnik["Polozka_" + str(idx)]["Cena"] = x.find("strong", {"class": "discount_price_value"}).text.strip()

            # Vypise mnozstvi
            # Odstraneni prebyecnych znaku .replace(u'\xa0', u' ').replace("/ ", "")
            # pr.:
            print(x.find("div", {"class": "discount_amount left"}).text.strip().replace(u'\xa0', u' ').replace("/ ", ""))
            muj_slovnik["Polozka_" + str(idx)]["Mnozstvi"] = x.find("div", {"class": "discount_amount left"}).text.strip()

            # Vypise platnost slevy - vypise vsechny .text polozky v cele "td" strukture
            print(x.find("td", {"class": "text-left discounts_validity valid_discount"}).text.strip())
            muj_slovnik["Polozka_" + str(idx)]["Platnost"] = x.find("td", {"class": "text-left discounts_validity valid_discount"}).text.strip()

            # Vypise prazdny radek pro odsazeni jednotlivych obchodu
            print()

            idx += 1
    else:
        print("Pro dany produkt ted momentalne neni zadna sleva")
        print()

print(f"Muj slovnik:      {muj_slovnik}")

print()

# Vypise do konzole
for idx in range(len(muj_slovnik.keys())):

    zbozi = muj_slovnik["Polozka_" + str(idx)]["Zbozi"]
    obchod = muj_slovnik["Polozka_" + str(idx)]["Obchod"]
    cena =  muj_slovnik["Polozka_" + str(idx)]["Cena"]
    mnozstvi = muj_slovnik["Polozka_" + str(idx)]["Mnozstvi"].replace(u'\xa0', u' ').replace("/ ", "")
    platnost = muj_slovnik["Polozka_" + str(idx)]["Platnost"]

    print(f"Zbozi: {zbozi}, Obchod: {obchod}, Cena: {cena}, Mnozstvi: {mnozstvi}, Trvani: {platnost}")


# Vypise textu do souboru
file = open("kupi.txt", "a")

for idx in range(len(muj_slovnik.keys())):

    zbozi = muj_slovnik["Polozka_" + str(idx)]["Zbozi"]
    obchod = muj_slovnik["Polozka_" + str(idx)]["Obchod"]
    cena =  muj_slovnik["Polozka_" + str(idx)]["Cena"]
    mnozstvi = muj_slovnik["Polozka_" + str(idx)]["Mnozstvi"].replace(u'\xa0', u' ').replace("/ ", "")
    platnost = muj_slovnik["Polozka_" + str(idx)]["Platnost"]

    file.write(f"Zbozi: {zbozi}, Obchod: {obchod}, Cena: {cena}, Mnozstvi: {mnozstvi}, Trvani: {platnost}" + "\n")

file.close()


################################################################################
# Emaily
################################################################################

# # Odsazeni od predchoziho textu
# print()

# username = 'martin.email.python@email.cz'
# password = 'Martin123'

# # Aby email fungoval hezky česky
# message = MIMEText(f"Obchod: {ob[0]}, Cena: {ob[1]}, Mnozstvi: {ob[2]}, Trvani: {ob[3]}")
# message['Subject'] = 'Kupi - slevy'  # Předmět
# message['From'] = username  # Od koho
# recipient = 'zurek.m@email.cz'  # Komu

# # Vytvoříme SMTP objekt se šifrováním pomocí SSL
# with smtplib.SMTP_SSL('smtp.seznam.cz', 465) as smtp:
#     print('Přihlašuji se...')
#     try:
#         smtp.login(username, password)
#     except Exception as e:
#         print('Přihlášení se nepovedlo.', e)
#         sys.exit()

#     print('Odesílám email...')
#     try:
#         smtp.sendmail(username, recipient, message.as_string())
#     except Exception as e:
#         print('Odeslání se nepovedlo.', e)
#         sys.exit()

#     print('OK')