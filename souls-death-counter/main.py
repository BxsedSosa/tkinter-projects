import json
import ttkbootstrap as ttk
from PIL import ImageTk, Image

root = ttk.Window(themename="cyborg")
root.title("Souls Death Counter")

death_count = ttk.IntVar()
boss_name = ttk.StringVar()
name_search = ttk.StringVar()


def increase_counter():
    current_count = death_count.get()
    current_count += 1
    death_count.set(current_count)


def decrase_counter():
    current_count = death_count.get()

    if current_count > 0:
        current_count -= 1
        death_count.set(current_count)


def write_to_json(data):
    with open("data.json", "r+") as file:
        file_data = json.load(file)
        file_data["boss"].append(data)
        file.seek(0)
        json.dump(file_data, file)


def read_from_json():
    with open("data.json", "r") as file:
        data = json.load(file)

    return data["boss"]


def search_name():
    name = name_search.get()
    boss_data = read_from_json()

    for data in boss_data:
        for boss in data.keys():
            if name == boss:
                change_gui_data(boss, data[boss]["death"])


def change_gui_data(name, curr_death_count):
    boss_name.set(name)
    death_count.set(curr_death_count)


pane = ttk.Frame(root).grid()
title = ttk.Label(pane, text="Elden Ring", font=("Arial", 25)).grid(
    row=0, column=0, pady=10, columnspan=2
)
img = ImageTk.PhotoImage(Image.open("logos/elden-ring.jpg"))
game_picture = ttk.Label(pane, image=img).grid(
    row=1, column=0, columnspan=2, padx=30, pady=5, sticky="we"
)
boss_title = ttk.Label(pane, textvariable=boss_name).grid(
    row=2, column=0, padx=30, pady=10, sticky="ws"
)
increment_count = ttk.Button(pane, command=increase_counter).grid(
    row=2, column=1, padx=30, pady=10, sticky="e"
)
counter = ttk.Label(pane, textvariable=death_count, font=("Arial", 40)).grid(
    row=3, column=0, padx=30, sticky="w"
)
decrement_count = ttk.Button(pane, command=decrase_counter).grid(
    row=3, column=1, padx=30, pady=10, sticky="e"
)
boss_search_text = ttk.Label(pane, text="Search:").grid(
    row=4, column=0, padx=30, pady=5, sticky="ws"
)
boss_search = ttk.Entry(pane, textvariable=name_search).grid(
    row=5, column=0, pady=10, padx=30, sticky="nw"
)
enter_search = ttk.Button(pane, text="Enter", command=search_name).grid(
    row=5, column=1, pady=10, padx=30, sticky="ne"
)

boss_name.set("hello")

root.mainloop()
