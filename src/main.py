# imports
from stl import mesh # creates and saves meshes
import time # used to time how long the computations take
import settings # PERSONAL library within directory that imports the settings
import interface # PERSONAL GUI script
import images # PERSONAL library for image processing and heightmap based on photo
import vertices # PERSONAL library for converting the heightmap into vertices

def main(): # manages GUI and calls other functions
    # all GUI
    MainMenu = interface.MainMenu()
    MainMenu.root.mainloop()
    
    # starts a timer to see how long calculations run
    start = time.time()

    # load commonly used temp settings
    temp_settings = interface.TEMP_SETTINGS # [x, y, thick, z, layer, image]
    
    # assigns the variables in the list to make easier to reference
    try: # catches if someone puts a letter into a textbox
        x = int(temp_settings[0])
        y = int(temp_settings[1])
        thickness = float(temp_settings[2])
        z = float(temp_settings[3])
        layer_height = float(temp_settings[4])
        image_name = temp_settings[5]
    except:
        print("Exiting. Please make sure to only enter integer or float values into settings.")
        exit()

    # Checks and/or Adjusts Resolution
    print("Loading image.")
    try: # tries to load the image.
        image = images.load_image(settings.IMAGE_PATH, image_name) # passes the path and name of the image and loads it
    except:
        print("The image name provided cannot be found. Make sure to check extension.")
        exit()

    print("Checking resolution.")
    if not images.check_resolution(x, y, layer_height, image): # if resoltuion is not okay
        print("Adjusting resolution.")
        image = images.adjust_resolution(x, y, layer_height, image, image_name) # adjusts resolution
    print("Resolution okay.")
    
    # Converts to Grayscale
    print("Converting to grayscale.")
    image = images.convert_grayscale(image, image_name)
    print("Conversion complete.")
    
    # Generates a Heightmap
    print("Generating heightmap.")
    heightmap = images.heightmap(image, thickness, layer_height, z, image_name)
    print("Heightmap complete.")

    # Formats the Vertices
    print("Formatting vertices.")
    faces = vertices.createFaces(heightmap)
    print("Done formatting vertices.")
    
    # Creates a mesh
    print("Creating STL.")
    vertices.createMesh(faces, image_name)

    final_time = (time.time() - start)
    print(f"Complete in {final_time} seconds.")

if __name__ == "__main__":
    main()
