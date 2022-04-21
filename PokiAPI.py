import requests

def retrieveMon(pokeName):
    """
    gets a dictionary of information from the pokeAPI for one pokemon

    :param name: Pokemon's name or pokedex number
    :returns: dictionary of information about the specified pokemon if successful; otherwise none
    """
    if pokeName is None:
        return
    pokeName = pokeName.lower().strip()
    if pokeName == '':
        return
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pokeName))

    print('Getting Pokemon Information...', end = '')
    
    if response.status_code == 200:
     print('Success!')
     return response.json()
    else:
     print('Fialed, Response code:',response.status_code)
     return

def pokeList(limit = 100000, offset=0):

    """
    gets a dictionary of information from the pokeAPI for one pokemon

    :param limit: how many pokemon to grab
    :param offset: which pokemon index at which to start
    :returns: a dictionary of a list of all pokemon grabbed; none if unsuccessful
    """
    params = {
        'offset':offset,
        'limit':limit
        }

    response = requests.get('https://pokeapi.co/api/v2/pokemon/', params=params )

    print('Getting a list of Pokemon...', end = '')
    
    if response.status_code == 200:
     print('Success!')
     pokedict = response.json()
     return [p['name']for p in pokedict['results']]#returns the name of every pokemon

    else:
     print('Fialed, Response code:',response.status_code)
     return

def retrieveMonsImage(pokeName):
    """
    gets the image of a pokemon

    :param name: Pokemon's name or pokedex number
    :returns: the image of the requested pokemon if successful; otherwise nothing
    """
    pokeDict = retrieveMon(pokeName)
    pokeUrl = pokeDict['sprites']['other']['official-artwork']['front_default']
    return pokeUrl