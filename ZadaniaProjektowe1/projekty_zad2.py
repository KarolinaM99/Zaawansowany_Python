import requests
from bs4 import BeautifulSoup

def losowy_artykul_wiki():
    url = "https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona"
    losowy_artykul = requests.get(url)
    return losowy_artykul.text  

def zapisz_do_pliku(losowy_artykul, nazwa_pliku):
    with open(nazwa_pliku, 'w', encoding='utf-8') as file:
        file.write(losowy_artykul)

def main():
    losowy_plik = losowy_artykul_wiki()
    bs = BeautifulSoup(losowy_plik, 'html.parser')
    tekst = bs.get_text()
    zapisz_do_pliku(tekst, "losowy_artykul_wiki.txt")

if __name__ == "__main__":
    main()
