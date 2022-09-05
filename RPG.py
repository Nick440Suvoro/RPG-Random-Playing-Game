import menu
import person

menu.read_file("Info.txt")

p = person.Player

p.my_name = input("\nКак тебя зовут, путник? ")

menu.main_menu(p)
