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

    # Método para recibir daño
    def recibir_dano(self, dano):
        self.__salud -= dano
        if self.__salud < 0:
            self.__salud = 0

    # Métodos de ataque y defensa
    def atacar(self):
        ataque = random.choice(self.__ataques)
        multiplicador = random.choice([0, 1, 1.5])
        return ataque * multiplicador

    def defender(self):
        defensa = random.choice(self.__defensas)
        multiplicador = random.choice([1, 0.5])
        return defensa * multiplicador