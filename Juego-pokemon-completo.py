import random

class Pokemon:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__salud = 100  # Salud inicial
        self.__ataques = [random.randint(0, 40) for _ in range(3)]
        self.__defensas = [random.randint(10, 35) for _ in range(2)]

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_salud(self):
        return self.__salud

    def get_ataques(self):
        return self.__ataques

    def get_defensas(self):
        return self.__defensas

    # Métodos de ataque y defensa
    def atacar(self):
        ataque = random.choice(self.__ataques)
        multiplicador = random.choice([0, 1, 1.5])
        return ataque * multiplicador

    def defender(self):
        defensa = random.choice(self.__defensas)
        multiplicador = random.choice([1, 0.5])
        return defensa * multiplicador

    # Método para realizar un turno de combate
    def recibir_dano(self, dano):
        self.__salud -= dano
        if self.__salud < 0:
            self.__salud = 0

# Función para realizar el combate
def combate(pokemon1, pokemon2):
    for turno in range(3):
        print(f"Turno {turno + 1}:")
        
        # Pokémon 1 ataca
        ataque1 = pokemon1.atacar()
        defensa2 = pokemon2.defender()
        if ataque1 > defensa2:
            dano = ataque1 - defensa2
            pokemon2.recibir_dano(dano)
            print(f"{pokemon1.get_nombre()} ataca a {pokemon2.get_nombre()} causando {dano} de daño.")
        else:
            print(f"{pokemon1.get_nombre()} ataca, pero {pokemon2.get_nombre()} se defiende.")

        # Pokémon 2 ataca
        ataque2 = pokemon2.atacar()
        defensa1 = pokemon1.defender()
        if ataque2 > defensa1:
            dano = ataque2 - defensa1
            pokemon1.recibir_dano(dano)
            print(f"{pokemon2.get_nombre()} ataca a {pokemon1.get_nombre()} causando {dano} de daño.")
        else:
            print(f"{pokemon2.get_nombre()} ataca, pero {pokemon1.get_nombre()} se defiende.")

        print(f"Salud de {pokemon1.get_nombre()}: {pokemon1.get_salud()}")
        print(f"Salud de {pokemon2.get_nombre()}: {pokemon2.get_salud()}")
        print("-" * 30)

    # Determinar el ganador
    if pokemon1.get_salud() > pokemon2.get_salud():
        print(f"{pokemon1.get_nombre()} gana!")
    elif pokemon2.get_salud() > pokemon1.get_salud():
        print(f"{pokemon2.get_nombre()} gana!")
    else:
        print("¡Es un empate!")

# Ejemplo de uso
if __name__ == "__main__":
    nombre1 = input("Ingrese el nombre del Pokémon 1: ")
    tipo1 = input("Ingrese el tipo del Pokémon 1: ")
    pokemon1 = Pokemon(nombre1, tipo1)

    nombre2 = input("Ingrese el nombre del Pokémon 2: ")
    tipo2 = input("Ingrese el tipo del Pokémon 2: ")
    pokemon2 = Pokemon(nombre2, tipo2)

    combate(pokemon1, pokemon2)