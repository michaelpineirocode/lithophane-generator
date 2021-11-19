# Manages the GUI

# imports
import tkinter as tk
from settings import * # use the settings namespace because it is called so often!

# global
TEMP_SETTINGS = None

# a window for the main menu
class MainMenu():
    def __init__(self):
        # window settings
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_X}x{WINDOW_Y}") # sets window dimensions
        self.root.resizable(False, False) # makes it so that the window cannot be resized
        self.root.title(WINDOW_TITLE) # assigns the title

        # building the widgets
        # header
        header = tk.Label(self.root, text="Michael Pineiro's Lithophane Generator")
        header.config(font=(FONT, HEADER_SIZE))
        
        # options
        thickness_label = tk.Label(self.root, text="Thickness")
        self.thickness_entry = tk.Entry(self.root)
        self.thickness_entry.insert(tk.END, str(THICKNESS))
        max_x_label = tk.Label(self.root, text="Max X")
        self.max_x_entry = tk.Entry(self.root)
        self.max_x_entry.insert(tk.END, str(MAX_X)) # inserts the default value from settings
        max_y_label = tk.Label(self.root, text="Max Y")
        self.max_y_entry = tk.Entry(self.root)
        self.max_y_entry.insert(tk.END, str(MAX_Y))
        z_scale_label = tk.Label(self.root, text="Z Scale")
        self.z_scale = tk.Scale(self.root, from_=0.5, to=2, orient=tk.HORIZONTAL, digits=3, resolution = 0.01, length=200)
        self.z_scale.set(Z_SCALE) # sets the scale to start at 1 by default
        image_name_label = tk.Label(self.root, text="Image Name") 
        self.image_name_entry = tk.Entry(self.root)
        
        # buttons
        settings_button = tk.Button(self.root, text= "Settings", command= lambda: self.openSettings())
        start_button = tk.Button(self.root, text = "Generate Lithophane!", height = 3, command = lambda: self.export())

        # pack to GUI (in order of how they appear)
        header.pack()
        
        thickness_label.pack()
        self.thickness_entry.pack()
        max_x_label.pack()
        self.max_x_entry.pack()
        max_y_label.pack()
        self.max_y_entry.pack()
        image_name_label.pack()
        self.image_name_entry.pack()
        z_scale_label.pack()
        self.z_scale.pack()
        
        start_button.pack(expand= True)
        settings_button.pack()

        self.menu = None

    def openSettings(self): # opens a new window with settings if button is pushed
        self.menu = SettingsMenu(self)
        self.menu.root.mainloop()

    def export(self): # reassigns the global temp settings to be used in another file
        global TEMP_SETTINGS # allows TEMP_SETTINGS to be rewritten
        TEMP_SETTINGS = [
            self.max_x_entry.get(), 
            self.max_y_entry.get(), 
            self.thickness_entry.get(), 
            self.z_scale.get(), 
            retrieve("printer", "layer_height"), 
            self.image_name_entry.get()
            ]
        
        # DESTROYS the menus (no more gui)
        try:
            # if statement won't work in case the settings are opened and closed. (object exists but the root has already been ended)
            self.menu.root.destroy() 
        except:
            pass # will prevent exceptions from being printed to console
        finally:
            self.root.destroy()

# a window for the settings and adjustments
class SettingsMenu:
    def __init__(self, mainmenu):
        # inherits the mainmenu to be able to modify the entry values upon saving settings
        self.mainmenu = mainmenu
    
         # window settings
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_X}x{S_WINDOW_Y}") # sets window dimensions
        self.root.resizable(False, False) # makes it so that the window cannot be resized
        self.root.title(WINDOW_TITLE) # assigns the title

        # building the widgets
        # header
        header = tk.Label(self.root, text="Settings")
        header.config(font=(FONT, HEADER_SIZE))
        caption = tk.Label(self.root, text="Set the default settings that the program will use next time it is loaded.")
        caption.config(font=(FONT, 12))

        # user options
        thickness_label = tk.Label(self.root, text="Thickness")
        self.thickness_entry = tk.Entry(self.root)
        self.thickness_entry.insert(tk.END, str(THICKNESS))
        max_x_label = tk.Label(self.root, text="Max X")
        self.max_x_entry = tk.Entry(self.root)
        self.max_x_entry.insert(tk.END, str(MAX_X)) # inserts the default value from settings
        max_y_label = tk.Label(self.root, text="Max Y")
        self.max_y_entry = tk.Entry(self.root)
        self.max_y_entry.insert(tk.END, str(MAX_Y))
        z_scale_label = tk.Label(self.root, text="Z Scale")
        self.z_scale = tk.Scale(self.root, from_=0.5, to=2, orient=tk.HORIZONTAL, digits=3, resolution = 0.01, length=200)
        self.z_scale.set(Z_SCALE) # sets the scale to start at 1 by default
        output_label = tk.Label(self.root, text="Output Path(from project directory)")
        self.output_entry = tk.Entry(self.root)
        self.output_entry.insert(tk.END, str(OUTPUT))
        
        # printer options
        printer_name_label = tk.Label(self.root, text = "Printer Name")
        self.printer_name_entry = tk.Entry(self.root)
        self.printer_name_entry.insert(tk.END, P_NAME)
        bed_x_label = tk.Label(self.root, text = "Bed Size X (mm)")
        self.bed_x_entry = tk.Entry(self.root)
        self.bed_x_entry.insert(tk.END, str(BED_X))
        bed_y_label = tk.Label(self.root, text = "Bed Size Y (mm)")        
        self.bed_y_entry = tk.Entry(self.root)
        self.bed_y_entry.insert(tk.END, str(BED_Y))
        layer_height_label = tk.Label(self.root, text="Layer Height (mm)")
        self.layer_height_entry = tk.Entry(self.root)
        self.layer_height_entry.insert(tk.END, str(LAYER_HEIGHT))

        # buttons
        save_button = tk.Button(self.root, text = "Save", command= lambda: self.compile_settings(False))
        save_and_load = tk.Button(self.root, text="Save and Modify", command = lambda: self.compile_settings(True))

        # packing 
        header.pack()
        caption.pack()
        
        thickness_label.pack()
        self.thickness_entry.pack()
        max_x_label.pack()
        self.max_x_entry.pack()
        max_y_label.pack()
        self.max_y_entry.pack()
        z_scale_label.pack()
        self.z_scale.pack()
        output_label.pack()
        self.output_entry.pack()

        printer_name_label.pack()
        self.printer_name_entry.pack()
        #bed_x_label.pack()
        #self.bed_x_entry.pack()
        #bed_y_label.pack()
        #self.bed_y_entry.pack()
        layer_height_label.pack()
        self.layer_height_entry.pack()

        save_button.pack(side = tk.LEFT)
        save_and_load.pack(side = tk.RIGHT)

    def compile_settings(self, reenter): # this function gets the current value out of every widget and stores it as a list
        n_user_options = [self.max_x_entry.get(), self.max_y_entry.get(), self.thickness_entry.get(), self.z_scale.get(), self.output_entry.get()]
        n_printer_options = [self.printer_name_entry.get(), self.bed_x_entry.get(), self.bed_y_entry.get(), self.layer_height_entry.get()]
        self.save(n_user_options, n_printer_options) # edits the settings.json file
        if reenter: # if they press the reload button
            self.reload() # reloads all the settings to be curren
    
    def reload(self):
        # deletes old values
        self.mainmenu.thickness_entry.delete(0, "end")
        self.mainmenu.max_x_entry.delete(0, "end")
        self.mainmenu.max_y_entry.delete(0, "end")

        # reassigns new values
        self.mainmenu.thickness_entry.insert(tk.END, str(retrieve("user", "thickness"))) # needs to retrieve new value from save file
        self.mainmenu.max_x_entry.insert(tk.END, str(retrieve("user", "max_x")))
        self.mainmenu.max_y_entry.insert(tk.END, str(retrieve("user", "max_y")))
        self.mainmenu.z_scale.set(retrieve("user", "z_scale"))

    def save(self, n_user_options, n_printer_options):
       # n_user and n_printer options are lists of all the current options values (new values)
       
        # we save the current user options as a dictionary to be able to pull the value and where the settings
        # should look to update the json
        user_options = {"max_x": MAX_X, "max_y": MAX_Y, "thickness": THICKNESS, "z_scale": {Z_SCALE}, "output": OUTPUT}
        printer_options = {"name": P_NAME, "bed_x": BED_X, "bed_y": BED_Y, "layer_height": LAYER_HEIGHT}
        
        inc = 0 # we need to keep count of how far we are in the dictionary
        for option in user_options:
            new_option = n_user_options[inc]
            if user_options[option] != new_option: # only update if the value changed
                update("user", option, new_option)
            inc += 1

        inc = 0 # resets the variable for a new loop
        for option in printer_options:
            new_option = n_printer_options[inc]
            if printer_options[option] != new_option:
                update("printer", option, new_option)
            inc += 1
