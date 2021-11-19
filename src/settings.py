# Imports and exports different settings from
# /settings/settings.json. This is to save the
# users 3D printer settings.

# libraries
import json # used to edit the json of settings

SETTINGS_PATH = "settings/settings.json"

def retrieve(header, element): # retrieves settings from the json file
    file = open(SETTINGS_PATH)
    data = json.load(file)
    ret = data[header][0][element] # finds the setting and returns its value
    return ret

def update(header, element, new): # saves settings to the json file
    file = open(SETTINGS_PATH, "r") # opens json file
    data = json.load(file) # loads into memorty
    file.close()
    data[header][0][element] = new # reassigns the old value to the new one
   
    file = open(SETTINGS_PATH, "w") # reopens
    json.dump(data, file, indent = 4) # writes new data
    file.close()

# GLOBALS TO EXPORT
# USER SETTINGS / INDIVIDUAL PRINTS
MAX_X = retrieve("user", "max_x") # sets a limitation so that the input can be reduced in size if possible
MAX_Y = retrieve("user", "max_y") 
THICKNESS = retrieve("user", "thickness") # the thickness that the lithophane should be
Z_SCALE = retrieve("user", "z_scale") # an amplifier to make the peaks and valleys further if wanted
OUTPUT = retrieve("user", "output_path")

# PRINTER SETTINGS
P_NAME = retrieve("printer", "name")
LAYER_HEIGHT = retrieve("printer", "layer_height") # how physically large in mm the printer will print each layer
BED_X = retrieve("printer", "bed_x") # dimensions of the size of the printer bed
BED_Y = retrieve("printer", "bed_y")

# Other random settings (cannot be edited in GUI)
# paths and files
TEMP_SETTINGS = "temp/temp_settings" # file
RESOLUTION_PATH = "temp/resolution/" # path
GRAYSALE_PATH = "temp/grayscale/" # path
HEIGHTMAP_PATH = "temp/heightmap/" # path
IMAGE_PATH = "temp/inputs/" # path
OUTPUT_PATH = "STLS/"

DIVISOR = "!##!" # random string that will be used to divide items in a list
EXTENSION = ".jpeg" # the default output extension

#########################################################################
# GUI Settings (cannot be edited in the GUI)
WINDOW_TITLE = "Lithophane Generator"
WINDOW_X = 640
WINDOW_Y = 400
S_WINDOW_Y = 450 # length of the settings window
FONT = "Helvetica"
HEADER_SIZE = 30
TEXT_SIZE = 15

##########################################################################
# Utility settings / settings for development
GENERATE_HEIGHTMAP = True
