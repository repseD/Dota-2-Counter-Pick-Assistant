from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Node:
    def __init__(self, text: str, img_num: int, to_yes: int = None, to_no: int = None): # = None
        self.to_yes = to_yes
        self.to_no = to_no
        self.text: str = text
        self.img_num: int = img_num


frame: Frame
elements: list[Node] = [
    Node("Pos 1 - герой ближнего боя?", 1, 1, 21),
    Node("Этот герой - Sven?", 2, 2, 4),
    Node("У него есть linkens sphere?", 3, 3, 32),
    Node("У него есть Satanic?", 4, 30, 31),
    Node("Этот герой - Lifestealer?", 5, 5, 9),
    Node("У него есть Blade Mail?", 6, 6, 34),
    Node("У него есть Mirror shield?", 7, 7, 8),
    Node("У него есть linkens sphere?", 8, 33, 34),
    Node("У него есть Satanic?", 9, 35, 34),
    Node("Этот герой - Phantom Assassin?", 10, 10, 14),
    Node("Вы - pos 3?", 11, 11, 12),
    Node("Хотите иметь высокую живучесть?", 12, 38, 39),
    Node("Вы - pos 1?", 13, 40, 13),
    Node("Вы - pos 4?", 14, 41, 42),
    Node("Этот герой - Wraith King?", 15, 15, 17),
    Node("У него Aghanim Shard куплен?", 16, 16, 45),
    Node("У него МКБ куплен?", 17, 43, 44),
    Node("Этот герой - Slark?", 18, 18, 60),
    Node("У него есть Lotus Orb?", 19, 19, 49),
    Node("У него есть БКБ?", 20, 46, 20),
    Node("У него есть Eternal shoud?", 21, 47, 48),
    Node("Pos 1 - герой дальнего боя?", 22, 22, 60),
    Node("Этот герой - Drow Ranger?", 23, 23, 25),
    Node("Вы - pos 3?", 24, 24, 58),
    Node("Играете агрессивно?", 25, 51, 52),
    Node("Этот герой - Luna?", 26, 26, 28),
    Node("Во вражеской команде есть Omniknight?", 27, 27, 56),
    Node("Во вражеской команде есть oracle?", 28, 54, 55),
    Node("Этот герой - Medusa?", 29, 29, 60),
    Node("Вы - pos 1?", 30, 57, 58),


    Node("Slardar\nСборка через moon shard и бесконечные станы способна остановить что угодно.", 31),
    Node("Troll Warlord\nБессмертие, оцепенение и огромная скорость атаки с чудовищным вампиризмом позволит эффективно противостоять кому угодно, и отыгрывать любую роль.", 32),
    Node("OD\nКража маны, являющаяся дизейблом, при полном отсутствии отражающих способностей у врага и огромный урон OD делают его грозным противником.", 33),
    Node("Bane\n4 направленных способности, полное отключение урона у 1 позиции и стан сквозь БКБ с поддержкой команды - грозная сила.", 34),
    Node("WR\nНаправленное связывание, покупаем предмет на оцепенение, ульт - от нас не скроется никто.", 35),
    Node("Terrorblade\nНемного здоровья, но много брони! В определенный момент демонов-иллюзий станет настолько много, что он может в одиночку воевать с целой армией.", 36),
    Node("WR\nНаправленное связывание, покупаем предмет на оцепенение, ульт - от нас не скроется никто.", 37),
    Node("WR\nНаправленное связывание, покупаем предмет на оцепенение, ульт - от нас не скроется никто.", 38),
    Node("Axe\nЕму безразлично: купил ли ты БКБ, сопротивление эффектам, ещё что-нибудь ... Провокация, обратный урон - всё.", 39),
    Node("Viper\nОтравит кого угодно, даже тех кто осмелится на него напасть. А отключение пассивных способностей - последний гвоздь в крышку гроба.", 40),
    Node("Slark\nНе прерываемая и не раскрываемая невидимость, развеивание почти всех негативных эффектов в игре, кража статов - идеальный вариант.", 41),
    Node("Omniknight\nСпаситель: полный иммунитет к физическому урону, лечение, полная защита от негативных эффектов - нужно ли больше?", 42),
    Node("Ember Spirit\nБыстрый удар, быстрый урон, быстрый фраг. Быстрый как языки пламени. Он и есть пламя.", 43),
    Node("Terrorblade\nНемного здоровья, но много брони! В определенный момент демонов-иллюзий станет настолько много, что он может в одиночку воевать с целой армией.", 44),
    Node("Phantom Lancer\nЦелая армия. Буквально. Стоит лишь ему начать атаку, как рядом с ним появляются десятки копий его погибших собратьев ...", 45),
    Node("Antimage\nСтрашный сон всех магов, Отражающий щит, выжигание маны, и огромный урон в поздней стадии. Если ты маг, беги.", 46),
    Node("Axe\nЕму безразлично: купил ли ты БКБ, сопротивление эффектам, ещё что-нибудь ... Провокация, обратный урон - всё.", 47),
    Node("Enigma\nЧёрная дыра, засасывающая ваших врагов. А у вас они вообще были?", 48),
    Node("Invoker\nОдин из самых могущественных магов этого мира. Невероятно сложен, но если вы сможете обуздать его мощь - станете почти непобедимы.", 49),
    Node("Grimstroke\nЧернильный маг: и союзника защитит, и противника обезмолвит, и создаст себе свою собственную команду из сильных иллюзий.", 50),
    Node("К сожалению, вашего героя ещё нет в списке :(", 51),
    Node("Centaur Warruner\nГрубая сила и оглушающие удары. В пылу сражения наносит огромный урон как себе, так и врагу. К нему даже приближаться опасно.", 52),
    Node("Clokwerk\nМаленький, но проворный и хитрый механик, который не так прост как кажется. Своими механизмами может сделать так, что вы не поймёте что вообще произошло.", 53),
    Node("Sniper\nОгромная пушка, стреляющая дальше чем многие могут увидеть. ", 54),
    Node("Bane\n4 направленных способности, полное отключение урона у 1 позиции и стан сквозь БКБ с поддержкой команды - грозная сила.", 55),
    Node("Timbersaw\nЧем больше его бьёшь - тем меньше его бьёшь. А смертоносные пилы не дадут подойти близко.", 56),
    Node("Bristleback\nЁж. Потревожь его - получишь столько иголок, что хватит до конца жизни.", 57),
    Node("Antimage\nСтрашный сон всех магов, Отражающий щит, выжигание маны, и огромный урон в поздней стадии. Если ты маг, беги.", 58),
    Node("Sniper\nОгромная пушка, стреляющая дальше чем многие могут увидеть.", 59),
    Node("К сожалению, вашего героя ещё нет в списке :(", 61),
    Node("К сожалению, наша экспертная система вам не подходит :(", 61)
]

answers_button_obj: list = []
main_window = Tk()
main_window.title("IZ-4")
main_height: int = 0
button_list = []
image_1 = None


def create_dialog(root: Node):
    global answers_button_obj
    for el in answers_button_obj:
        el.destroy()
    answers_button_obj = []
    new_label = None
    if root.to_yes is None and root.to_no is None:
        new_label = ttk.Label(frame, text="Ответ: " + root.text, wraplength=300)
    else:
        new_label = ttk.Label(frame, text=root.text, wraplength=300)
    new_label.pack(pady=10, anchor=CENTER)
    answers_button_obj.append(new_label)

    global image_1
    if image_1 is not None:
        image_1.destroy()
    img = Image.open(f'{root.img_num}.png')
    img = img.resize((500, 500))
    test = ImageTk.PhotoImage(img)
    image_1 = ttk.Label(image=test)
    image_1.image = test
    image_1.pack(anchor=CENTER)

    if root.to_yes is not None and root.to_no is not None:
        new_button = ttk.Button(frame, text="Да", command=lambda b=elements[root.to_yes]: create_dialog(b))
        new_button.pack(anchor=CENTER)
        answers_button_obj.append(new_button)

        new_button = ttk.Button(frame, text="Нет", command=lambda b=elements[root.to_no]: create_dialog(b))
        new_button.pack(anchor=CENTER)
        answers_button_obj.append(new_button)


# Create two frames for the two columns
left_frame = ttk.Frame(main_window)
right_frame = ttk.Frame(main_window)
left_frame.pack(side=LEFT, fill=BOTH, expand=True)
right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Add the first 14 buttons to the left frame
for i in range(15):
    button = ttk.Button(left_frame, text=str(i + 1) + ". " + elements[i].text, width=50,
                        command=lambda b=elements[i]: create_dialog(b))
    button_list.append(button)
    button.pack(anchor=CENTER)

# Add the remaining buttons to the right frame
for i in range(15, 30):
    button = ttk.Button(right_frame, text=str(i + 1) + ". " + elements[i].text, width=50,
                        command=lambda b=elements[i]: create_dialog(b))
    button_list.append(button)
    button.pack(anchor=CENTER)

frame = ttk.Frame(main_window)
frame.pack(fill="both", anchor="center", expand=True, side=TOP)

main_window.geometry(f"1200x600")
main_window.resizable(width=False, height=False)
create_dialog(elements[0])
main_window.mainloop()
