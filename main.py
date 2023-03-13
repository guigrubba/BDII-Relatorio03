from database import Database
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")

pokedex = Pokedex(db)

pokedex.postPokemonByName("Bulbasaur")
pokedex.postPokemonByNumberWeakness(1)
pokedex.postPokemonByWeakness(["Psychic", "Ice"])
pokedex.postPokemonIntervalSpawn(0.3, 1)
pokedex.postPokemonsByType(["Grass", "Poison"])
