from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


CUSTOM_SEARCH_ENGINE_ID = os.getenv('CUSTOM_SEARCH_ENGINE_ID')

Kaggle_Token = os.getenv("Kaggle_Token")

SourceForge_API = os.getenv("SourceForge_API")

CodeBerg_API = os.getenv("CODEBERG_API")


def search(query):
    # Vérifiez que les informations de configuration sont correctement chargées
    if not GOOGLE_API_KEY or not CUSTOM_SEARCH_ENGINE_ID:
        raise ValueError(
            "GOOGLE_API_KEY and CUSTOM_SEARCH_ENGINE_ID must be set in the .env file"
        )

    # Construct the search URL using the Google Custom Search API
    url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={CUSTOM_SEARCH_ENGINE_ID}&q={query}"

    try:
        # Send a GET request to the search URL
        response = requests.get(url)

        # Analyze the JSON response
        data = json.loads(response.text)

        # Extract the relevant search results
        return [
            (item["title"], item["link"], item["snippet"]) for item in data["items"]
        ]

    except requests.exceptions.RequestException as e:
        # Gérez les erreurs potentielles en levant une exception personnalisée
        raise ValueError(f"Error while searching: {e}")


def search_github(query):
    url = f'https://api.github.com/search/repositories?q={query}&per_page=10'
    response = requests.get(url)
    data = response.json()
    results = []
    for item in data['items']:
        title = item['full_name']
        link = item['html_url']
        description = item['description'] if 'description' in item else ''
        results.append((title, link, description))
    return results


def search_gitlab(query):
    url = f'https://gitlab.com/api/v4/search?query={query}&per_page=10&search_type=repositories'
    response = requests.get(url)
    data = response.json()
    results = []
    for item in data['items']:
        title = item['name']
        link = item['web_url']
        description = item['description'] if 'description' in item else ''
        results.append((title, link, description))
    return results


def search_sourceforge(query):
    url = f'https://sourceforge.net/api/search/project?q={query}&fields=title,url,description'
    response = requests.get(url)
    data = response.json()
    results = []
    for item in data['result']:
        title = item['title']
        link = item['url']
        description = item['description'] if 'description' in item else ''
        results.append((title, link, description))
    return results


def search_codeberg(query):
    url = f'https://codeberg.org/api/v1/search/repos?q={query}&per_page=10'
    response = requests.get(url)
    data = response.json()
    results = []
    for item in data['items']:
        title = item['name']
        link = item['html_url']
        description = item['description'] if 'description' in item else ''
        results.append((title, link, description))
    return results


def search_launchpad(query):
    url = f'https://api.launchpad.net/devel/ubuntu/+search?searchon=names&search={query}'
    response = requests.get(url)
    data = response.json()
    results = []
    for item in data['items']:
        title = item['name']
        link = item['resource_path']
        description = item['description'] if 'description' in item else ''
        results.append((title, link, description))
    return results


def search_langchain(query):
    url = f'https://api.langchain.com/v1/search?q={query}&per_page=10'
    response = requests.get(url)
    data = response.json()
    results = []
    for item in data['items']:
        title = item['name']
        link = item['html_url']
        description = item['description'] if 'description' in item else ''
        results.append((title, link, description))
    return results


def search_huggingface(query):
    url = f'https://huggingface.co/api/datasets?search={query}&per_page=10'
    response = requests.get(url)
    data = response.json()
    results = []
    for item in data['results']:
        title = item['name']
        link = item['url']
        description = item['description'] if 'description' in item else ''
        results.append((title, link, description))
    return results


def search_pypi(query):
    url = f'https://pypi.org/pypi/{query}/json'
    response = requests.get(url)
    data = response.json()
    results = []
    if 'info' in data:
        title = data['info']['name']
        link = f'https://pypi.org/project/{title}/'
        description = data['info']['description'] if 'description' in data['info'] else ''
        results.append((title, link, description))
    return results


def search_kaggle(query):
    url = f'https://api.kaggle.com/api/v1/search/datasets?search={query}&sortBy=downloadCount&group=python&page=1&limit=10'
    headers = Kaggle_Token
    response = requests.get(url, headers=headers)
    data = response.json()
    results = []
    for item in data['results']:
        title = item['title']
        link = item['url']
        description = item['description'] if 'description' in item else ''
        results.append((title, link, description))
    return results


def search_all(query):
    search_functions = [
        search,
        search_github,
        search_gitlab,
        search_langchain,
        search_huggingface,
        search_kaggle,
        search_launchpad,
        search_pypi,
        search_codeberg
    ]
    results = []
    for search_function in search_functions:
        try:
            search_results = search_function(query)
            results.extend(search_results)
        except Exception as e:
            print(f"Error while calling {search_function.__name__}: {e}")
    return results
