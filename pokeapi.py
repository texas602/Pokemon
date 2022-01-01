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
        id = getId(data)
        name = getName(data)
        types = getTypes(data)
        height = getHeight(data)
        abilities = getAbilities(data)
        stats = getStats(data)
        return Pokemon(id,name,height,types,abilities,stats)

def getId(data):
    return str(data['id'])

def getName(data):
    return data['name']

def getTypes(data):
    types = []
    for x in data['types']:
        types.append(x['type']['name'])
    return types

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
