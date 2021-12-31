from pokeapi import pokeinfo

def dex(name):
    pokemon = pokeinfo(name)
    if pokemon != None:
        print('\nPokemon name is: ' + pokemon.name.capitalize())
        print('Height: ' + str(pokemon.height))
        print('Possible abilities: ')
        for x in pokemon.abilities:
            print('  '+ x)
        print('HP: ' + pokemon.stats['hp'])
        print('ATTACK: ' + pokemon.stats['attack'])
        print('DEFENSE: ' + pokemon.stats['defense'])
        print('SPECIAL-ATTACK: ' + pokemon.stats['special-attack'])
        print('SPECIAL-DEFENSE: ' + pokemon.stats['special-defense'])
        print('SPEED: ' + pokemon.stats['speed'])
    else:
        print('Pokemon does not exist within records')
