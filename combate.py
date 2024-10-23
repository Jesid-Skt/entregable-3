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