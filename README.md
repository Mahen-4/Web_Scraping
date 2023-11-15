# Web Scraping et Visualisation d'Animes

Ce projet utilise le web scraping pour extraire les données sur les meilleurs animes à partir du site MyAnimeList et les visualise dans un tableau .

## Prérequis

- Python 3.x
- Les bibliothèques Python : `requests`, `beautifulsoup4`, `pandas`, `matplotlib`

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

## Utilisation

1. Clonez le dépôt:

```bash
git clone https://github.com/votre-nom/utilisateur-anime.git
```

2. Accédez au répertoire du projet:

```bash
cd utilisateur-anime
```

3. Exécutez le script:

```bash
python scraping.py
```

## Fonctionnement

Le script récupère les données sur les meilleurs animes depuis [MyAnimeList](https://myanimelist.net/topanime.php), organise ces données dans un DataFrame (pandas), puis les affiche dans un tableau avec Matplotlib et Tkinter.

## Adaptabilité à d'autres sites

Le script a été conçu de manière simple, ce qui le rend facilement adaptable à d'autres sites web de classement d'animes avec des structures HTML différentes.
