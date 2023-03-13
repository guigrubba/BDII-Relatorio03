from helper.writeAJson import writeAJson
from database import Database

class Pokedex:
    def __init__(self, database: Database):
        self.db = database

    def postPokemonsByType(self, types: list): 
        pokemons = self.db.collection.find({"type": {"$in": types}})
        writeAJson(pokemons, "pokemons_by_types")
    
    def postPokemonByName(self, name):
        pokemon = self.db.collection.find({"name": name})
        writeAJson(pokemon, "pokemon_by_name")
    
    def postPokemonByWeakness(self, weakness: list):
        pokemons = self.db.collection.find({"weaknesses": {"$all": weakness}})
        writeAJson(pokemons, "pokemons_by_weakness") 
    
    def postPokemonByNumberWeakness(self, number):
        pokemons = self.db.collection.find({"weaknesses": {"$size": number}})
        writeAJson(pokemons, "pokemon_by_number_weakness")
    
    def postPokemonIntervalSpawn(self, spawn1, spawn2):
        pokemons = self.db.collection.find({"spawn_chance": {"$gt": spawn1, "$lt": spawn2}})
        writeAJson(pokemons, "pokemon_by_interval_spawn")
