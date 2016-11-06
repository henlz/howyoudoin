from json import loads
from random import choice

def catchthemall():
    file = open("./cantadas.json", 'r')
    string = str(file.read())
    cantadas = loads(string)
    result = choice(cantadas)
    return result

catchthemall()
