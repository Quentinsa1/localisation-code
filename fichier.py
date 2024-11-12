import requests

def rechercher_articles(terme, max_articles=3):
    url = "https://api.crossref.org/works"
    params = {
        "query": terme,
        "rows": max_articles,
        "sort": "relevance"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['message']['items']
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
        return None

articles = rechercher_articles("Traditional Food Systems and Biodiversity")
if articles:
    for article in articles:
        print(article['title'][0])
