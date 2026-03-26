from services.combat_service import iniciar_combate


def crear_player():
    nombre = input("name: ").strip()

    while nombre == "":
        print("nombre invalido")
        nombre = input("name: ").strip()

    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")

    opt = input("choose: ").strip()

    while opt not in ["1", "2", "3"]:
        print("opcion invalida")
        opt = input("choose: ").strip()

    if opt == "1":
        player = {
            "nombre": nombre,
            "vida": 150,
            "ataque": 18,
            "defensa": 10,
            "pociones": 2,
            "experiencia": 0,
            "oro": 0
        }

    elif opt == "2":
        player = {
            "nombre": nombre,
            "vida": 90,
            "ataque": 30,
            "defensa": 3,
            "pociones": 3,
            "experiencia": 0,
            "oro": 0
        }

    else:
        player = {
            "nombre": nombre,
            "vida": 110,
            "ataque": 22,
            "defensa": 6,
            "pociones": 2,
            "experiencia": 0,
            "oro": 0
        }

    return player


def main():
    player = crear_player()
    iniciar_combate(player)


if __name__ == "__main__":
    main()
