import requests
from requests.exceptions import HTTPError
import json
from pokemon import Pokemon


def requestInfo(name):
    try:
        response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(name))
        pokemon = json.loads(response.text)
        return pokemon

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        pass

def pokeinfo(name):
    data = requestInfo(name)
    if data != None:
        name = getName(data)
        height = getHeight(data)
        abilities = getAbilities(data)
        stats = getStats(data)
        return Pokemon(name,height,abilities,stats)


def getName(data):
    return data['name']

def getHeight(data):
    return data['height']

def getAbilities(data):
    abilities = []
    for x in data['abilities']:
        abilities.append(x['ability']['name'])
    return abilities

def getStats(data):
    stats = {}
    for x in data['stats']:
        stats[x['stat']['name']] = str(x['base_stat'])
    return stats
