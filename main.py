from pokemon import Pokemon
from combate import combate

def main():
    nombre1 = input("Ingrese el nombre del Pokémon 1: ")
    tipo1 = input("Ingrese el tipo del Pokémon 1: ")
    pokemon1 = Pokemon(nombre1, tipo1)

    nombre2 = input("Ingrese el nombre del Pokémon 2: ")
    tipo2 = input("Ingrese el tipo del Pokémon 2: ")
    pokemon2 = Pokemon(nombre2, tipo2)

    combate(pokemon1, pokemon2)

if __name__ == "__main__":
    main()
    