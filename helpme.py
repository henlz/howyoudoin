from json import loads
from random import choice

def catchthemall(pokemon=False, nerds=False):
    if pokemon:
        file = open("./pokemon.json", 'r')
    elif nerds:
        file = open("./nerds.json", 'r')
    else:
        file = open("./cantadas.json", 'r')
    string = str(file.read())
    cantadas = loads(string)
    result = choice(cantadas)
    return result

catchthemall()
