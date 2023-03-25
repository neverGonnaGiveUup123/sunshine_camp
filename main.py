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

        label_list = []
        buffer_list = []
        def update_button_func():
            label_list.clear()
            [i.destroy() for i in buffer_list]
            buffer_list.clear()

            if len(name_entry.get()) <= 1:
                error_label.config(text="A leader name must be provided!")
                return 0
            try:
                if int(number_of_campers_entry.get()) < 5 or int(number_of_campers_entry.get()) > 10:
                    error_label.config(text="Number of campers must be within 5 and 10!")
                    return 0
            except ValueError:
                error_label.config(text="Number of campers must be a number!")
                return 0
            else:
                error_label.config(text="No current errors.")

            data[name_entry.get()] = [location_entry.get(),number_of_campers_entry.get(),weather_entry.get()]
            for x,y in enumerate(data.keys()):
                group_label_list = []
                group_label_list.append(ttkb.Label(self,text=y))
                [group_label_list.append(ttkb.Label(self, text=j)) for j in data[y]]
                group_label_list.append(x)
                label_list.append(group_label_list)
            print(label_list)
            for a,b,c,d,x in label_list:
                a.grid(row=x+10,column=0)
                b.grid(row=x+10,column=1)
                c.grid(row=x+10,column=2)
                d.grid(row=x+10,column=3)

                buffer_list.append(b)
                buffer_list.append(c)
                buffer_list.append(d)
        
        def delete_button_func():
            try:
                data.pop(delete_entry.get())
            except KeyError:
                error_label.config(text="Leader name not found.")
            finally:
                error_label.config(text="Leader group deleted successfully. Remember to delete the entries!")

        update_button = ttkb.Button(self, text="Update information", bootstyle=INFO, command=update_button_func)
        update_button.grid(row=5,column=1,columnspan=2,padx=20,pady=20)

        delete_label = ttkb.Label(self,text="Enter leader name to delete group: ")
        delete_label.grid(row=6,column=1,padx=10,pady=10)
        delete_entry = ttkb.Entry(self)
        delete_entry.grid(row=6,column=2,padx=10,pady=10)
        delete_button = ttkb.Button(self, text="Delete group", bootstyle=DANGER, command=delete_button_func)
        delete_button.grid(row=7, column=1, columnspan=2, padx=10,pady=10)

        error_label = ttkb.Label(self, text="No current errors.")
        error_label.grid(row=8,column=1,columnspan=2,padx=10,pady=10)

        num_of_campers_output = ttkb.Label(self, text="Number of campers: ")
        num_of_campers_output.grid(row=9,column=2,padx=10,pady=5)

        location_output = ttkb.Label(self, text="Location: ")
        location_output.grid(row=9,column=1,padx=10,pady=5)

        weather_output = ttkb.Label(self, text="Weather: ")
        weather_output.grid(row=9,column=3,padx=10,pady=5)

        names_label = ttkb.Label(self, text="Names: ")
        names_label.grid(row=9, column=0, padx=10,pady=5)

app = sunshine_camp_gui()
app.mainloop()