import tkinter
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

class sunshine_camp_gui(ttkb.Window):
    def __init__(self) -> None:
        super().__init__()

        self.title("Sunshine camp practice assessment")
        # self.geometry("500x500")

        self.main_title = ttkb.Label(self, text="Sunshine Camp information recorder")
        self.main_title.config(font=('Helvetica', 14))
        self.main_title.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.name_label = ttkb.Label(self, text="Name: ")
        self.name_label.grid(column=0, row=1, padx=20, pady=10)

        self.name_entry = ttkb.Entry(self)
        self.name_entry.grid(column=1, row=1, padx=20, pady=10)

        self.location_label = ttkb.Label(self, text="Location: ")
        self.location_label.grid(row=2,column=0,padx=20,pady=10)

        self.location_entry = ttkb.Entry(self)
        self.location_entry.grid(row=2,column=1,padx=20,pady=10)

        self.number_of_campers_label = ttkb.Label(self, text="Number of campers: ")
        self.number_of_campers_label.grid(row=3,column=0,padx=20,pady=10)

        self.number_of_campers_entry = ttkb.Entry(self)
        self.number_of_campers_entry.grid(row=3, column=1, padx=20,pady=10)

        self.weather_label = ttkb.Label(self, text="Weather conditions: ")
        self.weather_label.grid(row=4, column=0, padx=20, pady=10)

        self.weather_entry = ttkb.Entry(self)
        self.weather_entry.grid(row=4, column=1, padx=20, pady=10)

app = sunshine_camp_gui()
app.mainloop()