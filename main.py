#import all the required libraries
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import datetime

#Create empty dict where data will be stored
data = {

}

class sunshine_camp_gui(ttkb.Window):
    #initialise class that inherits from ttkb.Window
    def __init__(self) -> None:
        #inherit all the methods of ttkb.Window
        super().__init__()

        #disable dragging, get current time and set window title
        self.resizable(False,False)
        self.date = datetime.datetime.now()
        self.title("Sunshine camp practice assessment")

        #create the main title
        main_title = ttkb.Label(self, text="Sunshine Camp info table")
        main_title.config(font=('Helvetica', 14))
        main_title.grid(row=0, column=2, pady=20)

        #create label for leader name entry
        name_label = ttkb.Label(self, text="Name: ")
        name_label.grid(column=1, row=1, pady=10)

        #create entry for leader names
        name_entry = ttkb.Entry(self)
        name_entry.grid(column=3, row=1, pady=10)

        #create label for location entry
        location_label = ttkb.Label(self, text="Location: ")
        location_label.grid(row=2,column=1,pady=10)

        #create entry for location
        location_entry = ttkb.Entry(self)
        location_entry.grid(row=2,column=3,pady=10)

        #create label for number of campers entry
        number_of_campers_label = ttkb.Label(self, text="Number of campers: ")
        number_of_campers_label.grid(row=3,column=1,pady=10)

        #create entry for number of campers
        number_of_campers_entry = ttkb.Entry(self)
        number_of_campers_entry.grid(row=3, column=3, pady=10)

        #create label for weather entry
        weather_label = ttkb.Label(self, text="Weather conditions: ")
        weather_label.grid(row=4, column=1,  pady=10)

        #create entry for weather
        weather_entry = ttkb.Entry(self)
        weather_entry.grid(row=4, column=3,  pady=10)

        def handle_label_grid():
            #loop through the data dict and assign a number to each key
            for x,y in enumerate(data.keys()):
                #Append all the table labels to group_label_list
                group_label_list = []
                group_label_list.append(ttkb.Label(self,text=y))
                [group_label_list.append(ttkb.Label(self, text=j)) for j in data[y]]
                group_label_list.append(x)
                group_label_list.append(ttkb.Label(self,text=f'{self.date.strftime("%a")} {self.date.strftime("%H")}:{self.date.strftime("%M")}'))
                label_list.append(group_label_list)

            for a,b,c,d,x,date in label_list:
                #grid all the labels onto the gui and store all labels in buffer_list
                a.grid(row=x+10,column=0)
                b.grid(row=x+10,column=1)
                c.grid(row=x+10,column=2)
                d.grid(row=x+10,column=3)
                date.grid(row=x+10,column=4)
                buffer_list.append(a)
                buffer_list.append(b)
                buffer_list.append(c)
                buffer_list.append(d)
                buffer_list.append(date)

        def clear_lists():
            #empty all the lists
            label_list.clear()
            [i.destroy() for i in buffer_list]
            buffer_list.clear()

        label_list = []
        buffer_list = []
        def update_button_func():
            #Check for invalid inputs
            clear_lists()
            if len(name_entry.get()) <= 1:
                error_label.config(text="A leader name must be provided!")
                handle_label_grid()
                return 0
            if len(location_entry.get()) <= 1:
                error_label.config(text='Location is required!')
                handle_label_grid()
                return 0
            if len(weather_entry.get()) <= 1:
                error_label.config(text='Weather is required!')
                handle_label_grid()
                return 0
            try:
                if int(number_of_campers_entry.get()) < 5 or int(number_of_campers_entry.get()) > 10:
                    error_label.config(text="Number must be within 5 and 10!")
                    handle_label_grid()
                    return 0
            except ValueError:
                error_label.config(text="Number of campers must be a number!")
                handle_label_grid()
                return 0
            else:
                error_label.config(text="No current errors.")
            
            #fetch the entries entered by the user
            data[name_entry.get()] = [location_entry.get(),number_of_campers_entry.get(),weather_entry.get()]
            handle_label_grid()
        
        def delete_button_func():
            #Delete the leader group that was entered
            try:
                data.pop(delete_entry.get())
            except KeyError:
                error_label.config(text="Leader name not found.")
            else:
                error_label.config(text="Group deleted successfully.")
                clear_lists()
                handle_label_grid()

        #Create the update button
        update_button = ttkb.Button(self, text="Update information", bootstyle=INFO, command=update_button_func)
        update_button.grid(row=5,column=2,pady=20)

        #Create the label, entry and button for delete group section
        delete_label = ttkb.Label(self,text="Enter name to delete group: ")
        delete_label.grid(row=6,column=1,pady=10)
        delete_entry = ttkb.Entry(self)
        delete_entry.grid(row=6,column=3,pady=10)
        delete_button = ttkb.Button(self, text="Delete group", bootstyle=DANGER, command=delete_button_func)
        delete_button.grid(row=7, column=2, pady=10)

        #Create the error label
        error_label = ttkb.Label(self, text="No current errors.")
        error_label.grid(row=8,column=2,pady=10)

        #Create the number of campers label where the number of campers will be dipslayed
        num_of_campers_output = ttkb.Label(self, text="Number of campers:")
        num_of_campers_output.grid(row=9,column=2,pady=5)

        #Create the location label where the location will be displayed
        location_output = ttkb.Label(self, text="Location:")
        location_output.grid(row=9,column=1,pady=5)

        #Create the weather label where the weather will be displayed
        weather_output = ttkb.Label(self, text="Weather:")
        weather_output.grid(row=9,column=3,pady=5)

        #create the names label where LEader names will be displayed
        names_label = ttkb.Label(self, text="Leader names:")
        names_label.grid(row=9, column=0, pady=5,padx=20)

        #create the time label where the time of the entry will be displayed
        time_of_entry_label = ttkb.Label(self, text="Time of entry:")
        time_of_entry_label.grid(row=9, column=4, pady=5, padx=20)

#if the file is being run directly (not being imported to another module)
if __name__ == '__main__':
    #create an abject of the gui
    app = sunshine_camp_gui()
    #display the gui
    app.mainloop()