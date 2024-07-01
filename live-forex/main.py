import ttkbootstrap as ttk

root = ttk.Window(themename="cyborg")
root.title("")

currency = ["Select", "USD", "EUR", "GBP"]
clicked_from = ttk.StringVar()
clicked_to = ttk.StringVar()

pane = ttk.Frame(root).grid()
title = ttk.Label(root, text="Curreny Converter").grid(row=0, column=0, sticky="e")
text_from = ttk.Label(root, text="FROM:").grid(row=1, column=0, sticky="w")
text_to = ttk.Label(root, text="TO:").grid(row=1, column=1, sticky="w")
drop_from = ttk.OptionMenu(root, clicked_from, *currency).grid(
    row=2, column=0, sticky="w"
)
drop_to = ttk.OptionMenu(root, clicked_to, *currency).grid(row=2, column=1, sticky="w")
text_amount = ttk.Label(root, text="AMOUNT:").grid(row=3, column=0, sticky="w")
input_amount = ttk.Entry(root).grid(row=4, column=0, columnspan=2)
text_conversion = ttk.Label(root, text="100 USD = 100 EUR").grid(
    row=5, column=0, sticky="w"
)
text_last_update = ttk.Label(root, text="Last Updated").grid(
    row=6, column=0, sticky="w"
)
btn_convert = ttk.Button(root, text="Convert").grid(row=7, column=0, sticky="w")

root.mainloop()
