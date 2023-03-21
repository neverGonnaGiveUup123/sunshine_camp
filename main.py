import tkinter
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

data = {

}

class sunshine_camp_gui(ttkb.Window):
    def __init__(self) -> None:
        super().__init__()

        self.title("Sunshine camp practice assessment")

        main_title = ttkb.Label(self, text="Sunshine Camp information recorder")
        main_title.config(font=('Helvetica', 14))
        main_title.grid(row=0, column=1, columnspan=2, padx=20, pady=20)

        name_label = ttkb.Label(self, text="Name: ")
        name_label.grid(column=1, row=1, padx=20, pady=10)

        name_entry = ttkb.Entry(self)
        name_entry.grid(column=2, row=1, padx=20, pady=10)

        location_label = ttkb.Label(self, text="Location: ")
        location_label.grid(row=2,column=1,padx=20,pady=10)

        location_entry = ttkb.Entry(self)
        location_entry.grid(row=2,column=2,padx=20,pady=10)

        number_of_campers_label = ttkb.Label(self, text="Number of campers: ")
        number_of_campers_label.grid(row=3,column=1,padx=20,pady=10)

        number_of_campers_entry = ttkb.Entry(self)
        number_of_campers_entry.grid(row=3, column=2, padx=20,pady=10)

        weather_label = ttkb.Label(self, text="Weather conditions: ")
        weather_label.grid(row=4, column=1, padx=20, pady=10)

        weather_entry = ttkb.Entry(self)
        weather_entry.grid(row=4, column=2, padx=20, pady=10)

        def update_button_func():
            data[name_entry.get()] = [location_entry.get(), number_of_campers_entry.get(), weather_entry.get()]
            for i in enumerate(data.keys()):
                ttkb.Label(self, text=i[1]).grid(row=i[0] + 7,column=0, pady=5)
                ttkb.Label(self, text=data[i[1]][0]).grid(row=i[0] + 7, column=1, pady=5)
                ttkb.Label(self, text=data[i[1]][1]).grid(row=i[0] + 7, column=2, pady=5)
                ttkb.Label(self, text=data[i[1]][2]).grid(row=i[0] + 7, column=3, pady=5)


        update_button = ttkb.Button(self, text="Update information", bootstyle=INFO, command=update_button_func)
        update_button.grid(row=5,column=1,columnspan=2,padx=20,pady=20)

        num_of_campers_output = ttkb.Label(self, text="Number of campers: ")
        num_of_campers_output.grid(row=6,column=2,padx=10,pady=5)

        location_output = ttkb.Label(self, text="Location: ")
        location_output.grid(row=6,column=1,padx=10,pady=5)

        weather_output = ttkb.Label(self, text="Weather: ")
        weather_output.grid(row=6,column=3,padx=10,pady=5)

        names_label = ttkb.Label(self, text="Names: ")
        names_label.grid(row=6, column=0, padx=10,pady=5)

app = sunshine_camp_gui()
app.mainloop()