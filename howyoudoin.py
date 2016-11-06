from json import loads
from random import choice

def howyoudoin():
    file = open("./cantadas.json", 'r')
    string = str(file.read())
    cantadas = loads(string)
    print(choice(cantadas))
