def create_enemy(nombre, vida, attack, defense, type):
    if not isinstance(nombre, str) or nombre.strip() == "":
        raise ValueError("nombre invalido")

    if not isinstance(vida, int) or vida <= 0:
        raise ValueError("vida invalida")

    if not isinstance(attack, int) or attack <= 0:
        raise ValueError("attack invalido")

    if not isinstance(defense, int) or defense < 0:
        raise ValueError("defense invalido")

    if not isinstance(type, str):
        raise ValueError("tipo invalido")

    enemy = {
        
        "nombre": nombre,
        "vida": vida,
        "attack": attack,
        "defense": defense, 
        "tipo": type
    }

    return enemy
     
