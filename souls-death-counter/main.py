import json
import ttkbootstrap as ttk
from PIL import ImageTk, Image

root = ttk.Window(themename="cyborg")
root.title("Souls Death Counter")
root.resizable(width=False, height=False)


death_count = ttk.IntVar()
boss_name = ttk.StringVar()
name_search = ttk.StringVar()


def increase_counter() -> None:
    current_count = death_count.get()
    current_count += 1
    death_count.set(current_count)


def decrase_counter() -> None:
    current_count = death_count.get()

    if current_count > 0:
        current_count -= 1
        death_count.set(current_count)


def save_new_data(name: str, death_counter: int) -> None:
    new_data = {name: {"death": death_counter}}

    with open("data.json", "r+") as file:
        file_data = json.load(file)
        file_data["boss"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


def update_existing_data(name: str, death_counter: int, key_idx: int) -> None:
    with open("data.json", "r+") as file:
        file_data = json.load(file)

        file_data["boss"][key_idx][name]["death"] = death_counter
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()


def update_last_used(name: str, death_counter: int):
    with open("data.json", "r+") as file:
        file_data = json.load(file)

        file_data["last_used"] = {name: {"death": death_counter}}
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()


def read_from_json() -> dict:
    with open("data.json", "r") as file:
        data = json.load(file)

    return data


def search_name() -> None:
    current_name = boss_name.get()
    current_death_count = death_count.get()
    name = name_search.get()
    boss_data = read_from_json()

    for idx, data in enumerate(boss_data["boss"]):
        x = list(data.keys())
        if x[0] == name and name == current_name:
            update_existing_data(current_name, current_death_count, idx)
            change_gui_data(current_name, current_death_count)
            return

        if name in data:
            if current_name in data:
                update_existing_data(current_name, current_death_count, idx)

            change_gui_data(name, data[name]["death"])
            return

    save_new_data(name, 0)
    change_gui_data(name, 0)


def change_gui_data(name: str, curr_death_count: int) -> None:
    boss_name.set(name)
    death_count.set(curr_death_count)


def starting_data() -> None:
    data = read_from_json()
    name = list(data["last_used"].keys())
    death = data["last_used"][name[0]]["death"]

    boss_name.set(name[0])
    death_count.set(death)


def on_close() -> None:
    name = boss_name.get()
    counter = death_count.get()
    boss_data = read_from_json()

    for idx, data in enumerate(boss_data["boss"]):
        if name in data:
            update_existing_data(name, counter, idx)

    update_last_used(name, counter)
    root.destroy()


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
increment_count = ttk.Button(pane, text="+", command=increase_counter).grid(
    row=2, column=1, padx=30, sticky="es"
)
counter = ttk.Label(pane, textvariable=death_count, font=("Arial", 40)).grid(
    row=3, column=0, padx=30, sticky="w"
)
decrement_count = ttk.Button(pane, text="-", command=decrase_counter).grid(
    row=3, column=1, padx=30, sticky="ne"
)
boss_search_text = ttk.Label(pane, text="Search:").grid(
    row=4, column=0, padx=30, pady=5, sticky="ws"
)
boss_search = ttk.Entry(pane, textvariable=name_search).grid(
    row=5, column=0, pady=10, padx=30, sticky="e"
)
enter_search = ttk.Button(pane, text="Enter", command=search_name).grid(
    row=5, column=1, pady=10, padx=30, sticky="w"
)

starting_data()
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
