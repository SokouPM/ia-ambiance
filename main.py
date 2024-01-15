# EXEMPLE
# from langchain.llms import Ollama
#
# input = input("What is your question?")
# llm = Ollama(model="llama2")
# res = llm.predict(input)
# print(res)


import re
import ssl

import feedparser
from langchain.llms import Ollama


class PrintColors:  # Classe pour les couleurs des messages dans la console
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_news_data(url):  # Fonction pour récupérer les données d'un flux RSS
    ssl._create_default_https_context = ssl._create_unverified_context  # Désactive la vérification SSL
    # Utilise feedparser pour lire le flux RSS
    feed = feedparser.parse(url)

    # Extrait les titres et extraits des nouvelles
    news_data = [(entry.title, entry.summary) for entry in feed.entries]
    return news_data


def analyze_sentiment(title, excerpt):  # Fonction pour analyser un article et attribuer une note
    # Crée le prompt pour Ollama
    prompt = """
    The following is a news story with its title. Evaluate the sentiment of this news and headline on a
    scale from 1 to 10, 1 being the most negative and 10 the most positive.
    
    ONLY GIVE ONLY ONE NUMBER BETWEEN 1 AND 10, if you give anything else, the program will crash.
    """

    # Analyse le sentiment avec Ollama
    llm = Ollama(model="llama2")
    response = llm.predict(prompt + title + excerpt)

    print(f"{PrintColors.OKCYAN}{response}")

    # Extrait la note de la réponse
    sentiment_note = int(re.search(r'\d+', response).group())
    print(f"{PrintColors.OKGREEN}Note attribuée : {sentiment_note}/10")

    return sentiment_note


def main():
    media_sites = {
        'Le Monde': 'https://www.lemonde.fr/rss/une.xml',
        'Libération': 'https://www.liberation.fr/arc/outboundfeeds/rss-all/collection/accueil-une/?outputType=xml',
        # 'L\'Humanité': 'https://www.humanite.fr/' # ⚠️ Pas de flux RSS,
        'Le Figaro': 'https://www.lefigaro.fr/rss/figaro_actualites.xml'
    }
    media_sentiments = {}
    articles_limit = 3

    try:

        for media, url in media_sites.items():
            # Pour chaque média, appelle la fonction get_news_data pour récupérer les données
            news_data = get_news_data(url)

            # Crée une liste vide pour récupérer les notes de chaque article
            media_sentiments[media] = []

            print(" ")
            print(f"{PrintColors.ENDC}Analyse des sentiments pour {media}...")

            if len(news_data) > articles_limit:  # Si le nombre d'articles est supérieur à la limite
                print(
                    f"{PrintColors.OKGREEN}Nombre d'articles trouvé : {len(news_data)} (limitation à {articles_limit})")
                # Réduit le nombre d'articles à la limite
                news_data = news_data[:articles_limit]
            else:  # Si le nombre d'articles est inférieur ou égal à la limite
                print(f"{PrintColors.OKCYAN}Nombre d'articles trouvé : {len(news_data)}")
            print(" ")

            # Analyse le sentiment pour chaque article
            for i in range(0, len(news_data)):
                title, excerpt = news_data[
                    i]  # Extrait le titre et l'extrait de l'article et les stocke dans des variables
                print(f"{PrintColors.ENDC}Analyse de l'article : {title}")

                try:
                    sentiment_note = analyze_sentiment(title, excerpt)
                    media_sentiments[media].append(sentiment_note)
                except Exception as e:
                    print(
                        f"{PrintColors.FAIL}🚨 Erreur lors de l'analyse du sentiment pour l'article '{title}': {PrintColors.UNDERLINE}{e}"
                    )

                print(f"{PrintColors.ENDC}")

        # Calcule la note moyenne pour chaque média
        for media, sentiments in media_sentiments.items():
            print(f"{PrintColors.ENDC}Calcul de la moyenne des sentiments pour {media}...")
            if sentiments:  # Vérifie si la liste n'est pas vide
                average_sentiment = sum(sentiments) / len(sentiments)
                media_sentiments[media] = average_sentiment
                print(f"{PrintColors.OKGREEN}Moyenne des sentiments pour {media}: {round(average_sentiment, 2)}/10")
                print(" ")
            else:
                media_sentiments[media] = 0  # Attribue une valeur par défaut si la liste est vide
                print(f"{PrintColors.WARNING}Aucun article trouvé pour {media}")
                print(" ")

        # Calcule la moyenne globale
        overall_average_sentiment = sum(media_sentiments.values()) / len(media_sentiments)
        print(f"{PrintColors.UNDERLINE}{PrintColors.BOLD}Moyenne globale: {round(overall_average_sentiment, 2)}/10")

    except Exception as e:
        print(f"{PrintColors.FAIL}🚨 Erreur lors de l'éxécution du script : {PrintColors.UNDERLINE}{e}")


if __name__ == "__main__":
    main()
