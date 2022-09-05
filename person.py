from random import randint

enemy_name = ["Гигантская летучая мышь", "Орк", "ОМОН-скелет", "Рейдер", "Крыса", "Гигантский паук", "Зомби", "Роботизированное ведро", "Древний шахтёр", "Гном-волшебник"]
boss_name = ["Дракон", "Профессор Рик", "Механист", "Штурмотрон", "Культист", "Хукер", "Повелитель подземелья"]

class Player:
    my_name = ''
    hp = 100
    damage = 10
    kills = 0
    turn = 0
    boss_kills = 0


class Enemy:

    hp = randint(70, 160)
    damage = randint(6, 13)


class Boss:

    hp = 500
    damage = 25