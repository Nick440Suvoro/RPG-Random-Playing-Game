import person
from random import randint
import shutil
import sys


# import os.path

def menu_stats(p):
    print("МОЯ СТАТИСТИКА\n================================================")
    print(f"Твоё имя: {p.my_name}")
    print(f"hp: {p.hp}")
    print(f"damage: {p.damage}")
    print(f"Мобов убито: {p.kills}")
    print(f"Боссов убито: {p.boss_kills}")
    input("Продолжим...")


def menu_fight(p):
    e = person.Enemy()
    e.hp += p.kills * randint(0, 5)
    e.damage += p.kills * randint(0, 3)
    tmp = randint(0, 8)

    while p.hp > 0 or e.hp > 0:
        print("================================================")
        print(f"Твой hp: {p.hp}; Урон: {p.damage}")
        print(f"Враг: {person.enemy_name[tmp]}; hp: {e.hp}; Урон: {e.damage}")
        print("================================================")
        print("1)Ударить")
        print("2)Хил 1-5")

        n = int(input("Что делать: "))
        print("================================================")

        if n == 1:
            p.turn += 1
            e.hp -= p.damage
            p.hp -= e.damage
            print("ИДЁТ БИТВА!")

        if n == 2:

            p.turn += 1
            p.hp += randint(1, 5)
            print("ИСПОЛЬЗУЮ АПТЕЧКУ!")

            if p.hp > 100 + p.kills * 5 + 20 * p.boss_kills:
                p.hp = 100 + p.kills * 5 + 20 * p.boss_kills

        if p.hp < 0 or p.hp < 0 and e.hp < 0:
            print("Game OVER!!!")
            return 0

        if e.hp < 0 and p.hp > 0:
            print("FATALITY!!!")
            p.kills += 1
            p.damage += randint(0, 2)
            p.hp += p.kills * 2 + 10
            return 0


def menu_end(p):
    print("================================================")
    print(f"Прощай, {p.my_name}!")
    print(f'Твой рекорд: {p.kills}')
    print(f'Ты убил: {p.boss_kills} боссов')
    print(f'Ходов: {p.turn}')
    input()
    return


def menu_boss_fight(p):
    ult_tmp = 0
    tmp = randint(0, 6)
    b = person.Boss()
    b.hp += p.boss_kills * 25
    b.damage += p.boss_kills * 5
    while p.hp > 0 or b.hp > 0:
        print("================================================")
        print(f"Твой hp: {p.hp}; Урон: {p.damage}")
        print(f"Босс: {person.boss_name[tmp]}; hp: {b.hp}; Урон: {b.damage}")
        print("================================================")
        print("1)Ударить")
        print("2)Хил 1-5")
        print(f"3)Ульта{ult_tmp}")

        n = int(input("Что делать: "))
        print("================================================")

        if n == 1:
            ult_tmp += 1
            b.hp -= p.damage
            p.hp -= b.damage
            print("ИДЁТ ВЕЛИКАЯ БИТВА!!!!!")

        if n == 2:

            ult_tmp += 1
            p.hp += randint(1, 5)
            print("ИСПОЛЬЗУЮ АПТЕЧКУ!!!!!")

            if p.hp > 100 + p.kills * 5 + 20 * p.boss_kills:
                p.hp = 100 + p.kills * 5 + 20 * p.boss_kills

        if n == 3:
            b.hp -= ult_tmp
            p.hp -= b.damage // 2
            ult_tmp = 0
            print("ИСПОЛЬЗУЮ УЛЬТУ!!!!!")

        if p.hp < 0:
            print("Game OVER!!!")
            return 0

        if b.hp < 0:
            print("Эта битва станет легендой!\nFATALITY!!!")
            p.boss_kills += 1
            p.damage += randint(0, 5)
            p.hp += 20
            return 0


def main_menu(p):
    check = True

    while check is True:

        if p.hp < 0:
            menu_end(p)
            check = False
            return

        print("================================================")
        print("1) Сражаться")
        print("2) Статистика")
        print("3) Бой с боссом")
        print("4) Стартовый свиток")
        print("5) Выйти из подземелья...")

        n = int(input("Я жду... "))

        if n == 1:
            menu_fight(p)
        if n == 2:
            menu_stats(p)
        if n == 3:
            if p.kills % 10 == 0:
                print("----------INFO----------")
                print(
                    "Бой с боссом - это тяжёлое испытание!\nУльта - накапливается в течение всего сражения\nПосле каждого использования перезарядка!")
                print("------------------------")
                menu_boss_fight(p)
            else:
                print("Ты ещё не готов!")
                menu_fight(p)

        if n == 4:
            read_file("Info.txt")
            main_menu(p)

        if n == 5:
            menu_end(p)
            return


def read_file(S):
    with open(S, encoding='utf-8') as file:
        shutil.copyfileobj(file, sys.stdout)
    print("\n")

