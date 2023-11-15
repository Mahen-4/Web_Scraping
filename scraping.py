import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import json
from tkinter import Tk

#Récupère la largeur et hauteur de l'écran
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy() 

# site web scrapper
URL = "https://myanimelist.net/topanime.php"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
titles_filtered = []
scores_filtered = []

#Récupère les titres des animés
titles = soup.find_all("h3",class_="anime_ranking_h3")

#Récupère le score-label de chaque animés
scores = soup.find_all("td", class_="score")

#Ajoute les titre dans un array avec une limite de 40 titres
for title in titles:
   if(len(titles_filtered) > 40):break;
   titles_filtered.append(title.text.strip()) 

#Ajoute les scores dans un array avec une limite de 40 titres
for score in scores:
   if(len(scores_filtered) > 40):break;
   theScoreText = score.find("span", class_="score-label")
   if theScoreText is not None:
         scores_filtered.append(theScoreText.text.strip())

#crée un dictionnaire a partir des deux array
my_dict = dict(zip(titles_filtered, scores_filtered))

# Crée un json file contenant le dictionnaire  des animés avec leur titre et score
with open("titles.json", 'w') as json_file:
    json.dump(my_dict, json_file, indent=2)

# Crée un DataFrame depuis le dictionnaire
df = pd.DataFrame(list(my_dict.items()), columns=['Title', 'Score'])

#changement de l'odre d'affichage du score du dataFrame 
df_sorted = df.sort_values(by='Score', ascending= False)

# Ajouter une colonne "Index" au DataFrame
df_sorted['Index'] = df_sorted.index
# arranger les colonnes pour placer "Index" à l'avant
df_sorted = df_sorted[['Index', 'Title', 'Score']]

# Créer une table 
fig, ax = plt.subplots(figsize=(screen_width / 100, screen_height / 100))
table_data = [df_sorted.columns.tolist()] + df_sorted.values.tolist()
table = ax.table(cellText=table_data, loc='center', colLabels=None, cellLoc='center')

# Style de la table
table.auto_set_font_size(False)
table.set_fontsize(8)
table.auto_set_column_width([0, 1])
ax.axis('off')


plt.show()

