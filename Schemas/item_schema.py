import random
from schemas.enemy_schema import create_enemy


def validate_player(player):
    required = ["nombre", "vida", "ataque", "defensa", "pociones", "experiencia", "oro"]

    for key in required:
        if key not in player:
            raise ValueError(f"faltante: {key}")

    if player["vida"] <= 0:
        raise ValueError("vida jugador invalida")

    if player["ataque"] <= 0:
        raise ValueError("ataque jugador invalido")

    if player["defensa"] < 0:
        raise ValueError("defensa jugador invalida")


def get_random_enemy():
    enemies = [
        create_enemy("Goblin", 80, 15, 3, "debil"),
        create_enemy("Orco", 120, 20, 5, "normal"),
        create_enemy("Esqueleto", 95, 18, 4, "rapido"),
        create_enemy("Dragon", 200, 28, 8, "boss")
    ]
    return random.choice(enemies)


def iniciar_combate(player):
    validate_player(player)

    enemy = get_random_enemy()

    print("\n--- combate iniciado ---")
    print(f"enemigo: {enemy['nombre']}")

    turno = 1

    while player["vida"] > 0 and enemy["vida"] > 0:
        print(f"\nTurno {turno}")
        print(f"{player['nombre']} | vida: {player['vida']}")
        print(f"{enemy['nombre']} | vida: {enemy['vida']}")

        print("\n1. atacar")
        print("2. defender")
        print("3. usar pocion")
        print("4. huir")

        opcion = input(">> ").strip()

        if opcion not in ["1", "2", "3", "4"]:
            print("opcion invalida")
            continue

        extra_def = 0

        if opcion == "1":
            dmg = random.randint(10, player["ataque"]) - enemy["defense"]
            dmg = max(0, dmg)
            enemy["vida"] -= dmg
            print(f"damage: {dmg}")

        elif opcion == "2":
            extra_def = 5
            print("defensa activa")

        elif opcion == "3":
            if player["pociones"] > 0:
                heal = random.randint(20, 30)
                player["vida"] += heal
                player["pociones"] -= 1
                print(f"heal +{heal}")
            else:
                print("sin pociones")
                continue

        elif opcion == "4":
            print("escape")
            return

        # turno enemigo
        if enemy["vida"] > 0:
            action = random.choice(["atk", "atk", "def"])

            if action == "atk":
                dmg = random.randint(5, enemy["attack"]) - (player["defensa"] + extra_def)
                dmg = max(0, dmg)
                player["vida"] -= dmg
                print(f"enemy hit {dmg}")

            else:
                enemy["defense"] += 2
                print("enemy defend")

        if enemy["defense"] > 8:
            enemy["defense"] = 8

        turno += 1

    if player["vida"] <= 0:
        print("game over")
    else:
        print("victoria")
        player["experiencia"] += 50
        player["oro"] += 25
