# Lithophane 2

## Requirements
Running the project requires several modules. The easiest way to install this will be to open a terminal in the project directory and run ```pip3 install -r src/req.txt```. This will install the following modules:
tkinter
numpy
numpy-stl
pillow
    
It is possible that tkinter will be difficult to install. For me on an M1 chip Mac running Big Sur, running ```brew install python-tk``` worked.
\

## Adding Images For Input

An image is necessary for setup. I have provided two input images by the names of “highres.jpeg” and “dmb.jpg”. Additional input images can be added by moving an image into the “src/temp/inputs/” directory. Photos that have high contrast and would look good as a grayscale image are best.
\

## Running the project

To run the project, start the “main.py” script. This can be done by running ```python3 src/main.py``` in a terminal from the main project directory.
\

## Settings Explained

There are **two** sets of settings, **temporary** and **permanent**. When the program is started, **permanent** settings will automatically be loaded as default. The **temporary** settings are the settings which can be edited temporarily and will be used to generate the lithophane.

 To edit **permanent** settings, click on the settings button and edit in the new window accordingly. You can either click “save” which will save the permanent settings for the next time the program is loaded, or click “save and modify” which will adjust the temporary settings and save the permanent settings. After the settings are saved, close out of the new window.

To edit the **temporary** settings, adjust the values on the main menu. These will not be saved the next time you load the program.

**Thickness** - this is how thick the thickest part of the lithophane will be in millimeters. \
*Recommended Value: 2 or 3*

**Max X** - this is the ideal and maximum value of the X axis in millimeters. Depending on the resolution, this value may be smaller, but it cannot be any larger. This is to set a bound for how big the image should be on the X axis and have an approximate size to shoot for.\
*Recommended Value: Larger than Y if the image is landscape oriented*

**Max Y** - this is the ideal and maximum value of the Y axis in millimeters. Depending on the resolution, this value may be smaller, but it cannot be any larger. This is to set a bound for how big the image should be on the Y axis and have an approximate size to shoot for.\
*Recommended Value: Larger if the image is portrait oriented*

**Image Name** - the name of the image. Do not include the path. Include the file extension.

**Z Scale** - Exaggerates the differences between peaks and valleys.\
*Recommended Value: 1 to 1.2*

**Layer Height** - The layer height in mm that this model will be printed at.\
*Recommended Value: 0.12 (for 0.4mm nozzle)*

### Advanced Settings

**Output Path** - relative directory that the STL’s will be saved to.

**Printer Name** - The printer name for reference of the user. If the user has multiple different printers configured in different ways, the settings may be different.
\

## Running

Once the settings are filled out, you are good to go! Make sure that you include the file name. You can try with one of my example files, in this case I will be using “dmb.jpg”.
![](https://github.com/michaelpineirocode/lithophane-generator/blob/main/gitimages/Screen%20Shot%202021-11-19%20at%2011.58.56%20AM.png)

To generate a lithophane, click “Generate Lithophane!” and it will begin! The window will close but there will still be some output to the terminal / python interpreter.
\

## Optional Data

If there is an issue with the end result of the lithophane, you can check every step along the photo / heightmap conversion process manually by checking different folders in the “temp” directory. 
\

## Printing the Lithophane! 

After all the calculations are done, an STL file will be outputted to the “STLS/” directory, or another directory as defined in the settings. 

**NOTE:** The outputted STL is not automatically to scale. The final result is much larger than the values that are inputted. However, the result is **mathematically and geometrically** optimized for the values given at the beginning. All this means that the file will need to be scaled down in a slicer, but the ratio and proportions will be **mathematically and geometrically correct**.

1.) Start by loading the STL into a slicer. For this example I will be using Ultimaker Cura.
![](https://github.com/michaelpineirocode/lithophane-generator/blob/main/gitimages/Screen%20Shot%202021-11-19%20at%2011.46.42%20AM.png)
2.) Center the STL to the center of the bed
![](https://github.com/michaelpineirocode/lithophane-generator/blob/main/gitimages/Screen%20Shot%202021-11-19%20at%2011.47.52%20AM.png)
3.) Turn **OFF** uniform scaling and scale to the dimensions desired in the beginning (Max X is X, May Y as Y, thickness as Z). This will make the model the desired size.
![](https://github.com/michaelpineirocode/lithophane-generator/blob/main/gitimages/Screen%20Shot%202021-11-19%20at%2011.50.12%20AM.png)
4.) Make sure the layer height is the same as previously indicated.
![](https://github.com/michaelpineirocode/lithophane-generator/blob/main/gitimages/Screen%20Shot%202021-11-19%20at%2011.50.49%20AM.png)
5.) Make sure to disable supports and enable *“Z hop when retracted”* and *“Enable Retraction”*
![](https://github.com/michaelpineirocode/lithophane-generator/blob/main/gitimages/Screen%20Shot%202021-11-19%20at%2011.52.09%20AM.png)
6.) Slice and save the file. This may take up to a minute.
![](https://github.com/michaelpineirocode/lithophane-generator/blob/main/gitimages/Screen%20Shot%202021-11-19%20at%2011.53.38%20AM.png)
### Happy printing!

