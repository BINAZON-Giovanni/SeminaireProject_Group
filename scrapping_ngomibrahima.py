# scrapping_ngomibrahima.py
# Récupère titre, prix et disponibilité des livres de https://books.toscrape.com/

import requests                  # pour télécharger la page web
from bs4 import BeautifulSoup    # pour lire le HTML

url = "https://books.toscrape.com/"

response = requests.get(url)
response.encoding = "utf-8"      # pour que le symbole £ s'affiche bien
soup = BeautifulSoup(response.text, "html.parser")

# Chaque livre est dans une balise <article class="product_pod">
livres = soup.find_all("article", class_="product_pod")

for livre in livres:
    titre = livre.find("h3").find("a")["title"]
    prix = livre.find("p", class_="price_color").text
    dispo = livre.find("p", class_="availability").text.strip()
    print(f"{titre} | {prix} | {dispo}")

print(f"\n{len(livres)} livres récupérés.")