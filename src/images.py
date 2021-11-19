from PIL import Image, ImageOps # image processing
import settings
import math

def load_image(path, name):
    image = Image.open(f"{path}{name}")
    return image

# takes the maximum x, the maximum y, and the size of the image to see if it'll fit in the size with the layerheight.
# Returns bool
def check_resolution(x, y ,layer_height, image): 
    image_x, image_y = image.size
    if (x / layer_height) < image_x: # if the number of times the printer can pass on the x axis is larger than the resolution
        return False
    elif (y / layer_height) < image_y:
        return False
    else:
        return True

def adjust_resolution(x, y, layer_height, image, image_name="Temp"):
    # maximum possible pixels that will fit
    size = round(x / layer_height), round(y / layer_height)
    
    image = image.resize(size, Image.ANTIALIAS) # resizes the image
    image.save(f"{settings.RESOLUTION_PATH}{image_name}") # will save the image so that the creator can see what it looks like
    return image
    
def convert_grayscale(image, image_name="Temp"):
    image = ImageOps.grayscale(image)
    image.save(f"{settings.GRAYSALE_PATH}{image_name}")
    return image

# generates a heightmap based on the darkness of each pizel
def heightmap(image, thickness, layer_height, z_scale, image_name):
    height_resolution = thickness / layer_height # finds how many layers we can possibly stack
    increments = math.floor(255 / height_resolution) # finds how often to consider a new layer (RGB is 255)

    image_x, image_y = image.size # gets the x and y size of the image
    heightmap = [[0 for y in range(image_y)] for x in range(image_x)] # creates a 2D array of 0's for the size of the image
    image = image.load() # loads the DATA of the image into memory to be observed and manipulated

    for y in range(image_y): # loop through every pixel in the image
        for x in range(image_x):
            pixel = image[x, y] # this individual pixel
            heightmap[x][y] = abs(round((((255-pixel)) / (increments * z_scale)))) # converts the darkness of the pixel into a height
            if heightmap[x][y] == 0: # if there is no thickness
                heightmap[x][y] = 1 # gives it a thickness of 1 layer
    
    
    # create a text file with the heights (not neccesary, option can be changed in settings)
    if settings.GENERATE_HEIGHTMAP:
        image_name = image_name.split(".")[0]
        
        f = open(f"{settings.HEIGHTMAP_PATH}{image_name}", "w")
        for y in heightmap: # loops through every list in the 2D array
            f.writelines(str(y) + "\n") # writes the list as a new line to the file
        f.close()
    
    return heightmap
