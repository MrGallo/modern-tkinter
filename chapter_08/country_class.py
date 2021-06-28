from tkinter import *
from tkinter import ttk


class CountryApp:
    def __init__(self, parent, countries = None):
        if countries is None:
            countries = []
        
        self.parent = parent
        self.countries = countries
        self.country_population = {}
        self.country_codes = []
        self.country_names = []
        for code, name, pop in self.countries:
            self.country_population[code] = pop
            self.country_codes.append(code)
            self.country_names.append(name)

        self.status_bar_text = StringVar(value="Select a country.")
        self.country_choices = StringVar(value=self.country_names)

        self._widgets()
        self._grid()

    def _widgets(self):
        self.frame_main = ttk.Frame(self.parent, padding=[5, 3, 5, 3])
        
        self.frame_contents = ttk.Frame(self.frame_main)
        self.label_status_bar = ttk.Label(self.frame_main, text="hello", anchor="w")

        self.frame_send_gift = ttk.Frame(self.frame_contents, padding=[5])
        self.listbox_countries = Listbox(self.frame_send_gift, listvariable=self.country_choices)
        self.label_temp = ttk.Label(self.frame_send_gift, text="Right panel")

    def _grid(self):
        self.frame_main.grid(column=0, row=0, sticky=(N, E, W, S))
        self.frame_main.rowconfigure(0, weight=1)
        self.frame_main.rowconfigure(1, weight=1)
        self.frame_main.columnconfigure(0, weight=1)

        # main children
        self.frame_contents.grid(row=0, column=0, sticky=(N, E, W, S))
        self.frame_contents.rowconfigure(0, weight=1)
        self.frame_contents.columnconfigure(0, weight=0)
        self.frame_contents.columnconfigure(1, weight=3)

        self.label_status_bar.grid(row=1, column=0, sticky=(W, S, E))

        # contents children
        self.listbox_countries.grid(row=0, column=0, sticky=(N, E, W, S))
        self.frame_send_gift.grid(column=1, row=0, sticky=(N, W, S, E))

        # send gift children
        self.label_temp.grid(row=0, column=1)


    # def _bindings(self):
    #     self.listbox_countries.bind("<<ListboxSelect>>", )


if __name__ == "__main__":
    countries = [
        ("ca", "Canada", 12345),
        ("en", "England", 123456),
        ("us", "United States", 99999),
    ]

    root = Tk()
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    CountryApp(root, countries)
    root.mainloop()