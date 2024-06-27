import ttkbootstrap as ttk

root = ttk.Window(themename="darkly")
root.title("Mph / Kmh Converter")

title_name = ttk.StringVar()
text_entry = ttk.StringVar()
distance_conversion = ttk.StringVar()


def change_conversion():
    if title_name.get() == "Mph to Kmh":
        title_name.set("Kmh to Mph")
    else:
        title_name.set("Mph to Kmh")


def convert_to_mph(kmh):
    miles = round(int(kmh) * 0.62, 2)
    distance_conversion.set(f"Miles: {str(miles)}")
    text_entry.set("")


def convert_to_kmh(miles):
    kmh = round(int(miles) * 1.609344, 2)
    distance_conversion.set(f"Kilometers: {str(kmh)}")
    text_entry.set("")


def validate_input():
    input = text_entry.get()

    if not input.isnumeric():
        distance_conversion.set("This is not a number!")
        text_entry.set("")
    else:
        if title_name.get() == "Mph to Kmh":
            convert_to_kmh(input)
        else:
            convert_to_mph(input)


content = ttk.Frame(root).grid()
title = ttk.Label(content, textvariable=title_name).grid(
    row=0, column=0, columnspan=2, padx=5
)
distance_entry = ttk.Entry(content, textvariable=text_entry).grid(
    row=1, column=0, sticky="w"
)
calendar_btn = ttk.Button(content, text="c", command=change_conversion).grid(
    row=1, column=1, pady=10
)

converted_distance = ttk.Label(content, textvariable=distance_conversion).grid(
    row=2, column=0, columnspan=2
)

submit = ttk.Button(content, command=validate_input, text="Convert").grid(
    row=3, column=0, columnspan=2, padx=20, pady=10
)

title_name.set("Mph to Kmh")

root.mainloop()
