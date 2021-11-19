# This script deals with actually converting the heightmap into a 
# usable set of vertices and faces which can be converted to a mesh with
# the numpy-stl library. It is very complicated, hence the comments.

import numpy as np # used for processing vertices
from stl import stl, mesh # used for meshes
import settings

# a function that updates the current faces.
# faces are triangles that consist of three vertices.
# returns the list of faces (faces) and the new face_inc (face_inc)
# data is a 2d list of points [[x, y, z], [x, y, z], [x, y z]]
def addFace(faces, face_inc, data):
    faces["vectors"][face_inc] = np.array(data) # adds a face with new content
    face_inc += 1 # increments how many faces we've created
    return faces, face_inc # returns faces and the current index

# takes the heightmap as input
# loops through heightmap and adjusts np array (STL) based on X, Y and Z
# returns np array of dtype "mesh"
def createFaces(heightmap):
    # number of faces. First term is total of faces on top. Second are the SIDES on X axis. Third is ??. Fourth is the bottom two.
    face_num = (((len(heightmap[0]) - 1) * (len(heightmap) - 1)) * 2) + (((len(heightmap[0]) - 1) * 4) + ((len(heightmap) - 1) * 5)) + 2
    faces = np.zeros(face_num, dtype=mesh.Mesh.dtype)
    face_inc = 0 # keeps track of how many faces deep we are
    
    # create image section
    for y in range(len(heightmap)):
        if y != len(heightmap) - 1: # last row is designated for creating the sides (solves weird indexing issue)
            for x in range(len(heightmap[y])):
                if x != len(heightmap[y]) - 1:
                    faces, face_inc = addFace(faces, face_inc, [[x, y, heightmap[y][x]], [x, y+1, heightmap[y+1][x]], [x+1, y, heightmap[y][x+1]]]) #creates first face (triangle)
                    faces, face_inc = addFace(faces, face_inc, ([[x, y+1, heightmap[y+1][x]], [x+1, y+1, heightmap[y+1][x+1]], [x+1, y, heightmap[y][x+1]]])) # creates second half of face (square)
    
    # create the sides and bottom of the STL
    # note: the reason that we need to loop through every pixel along the sides is because
    # each spot along the edge can potentially be a different height. In order for a slicer to
    # use the file, there cannot be any "spaces."
    
    # y axis SIDES
    for y in range(len(heightmap)):
        row_size = len(heightmap[y]) - 1
        # one side
        faces, face_inc = addFace(faces, face_inc, [[0, y, heightmap[y][0]], [0, y, 0], [0, y+1, heightmap[y][0]]])
        faces, face_inc = addFace(faces, face_inc, [[0, y+1, heightmap[y][0]], [0, y, 0], [0, y+1, 0]])
        # the opposite side
        faces, face_inc = addFace(faces, face_inc, [[row_size, y, heightmap[y][row_size]], [row_size, y, 0], [row_size, y+1, heightmap[y][0]]])
        faces, face_inc = addFace(faces, face_inc, [[row_size, y+1, heightmap[y][row_size]], [row_size, y, 0], [row_size, y+1, 0]])

    # x axis SIDES
    for x in range(len(heightmap[0])):
        col_size = len(heightmap) - 1
        # one side
        faces, face_inc = addFace(faces, face_inc, [[x, 0, heightmap[0][x]], [x, 0, 0], [x+1, 0, heightmap[0][x]]])
        faces, face_inc = addFace(faces, face_inc, [[x+1, 0, heightmap[0][x]], [x, 0, 0], [x+1, 0, 0]])
        # the opposite side
        faces, face_inc = addFace(faces, face_inc, [[x, col_size, heightmap[col_size][x]], [x, col_size, 0], [x+1, col_size, heightmap[0][x]]]) # sides furthest from 0 index
        faces, face_inc = addFace(faces, face_inc, [[x+1, col_size, heightmap[col_size][x]], [x, col_size, 0], [x+1, col_size, 0]])

    # the bottom
    faces, face_inc = addFace(faces, face_inc, [[0, 0, 0], [row_size, 0, 0], [0, col_size, 0]])
    faces, face_inc = addFace(faces, face_inc, [[row_size, col_size, 0], [row_size, 0, 0], [0, col_size, 0]])

    return faces

# actually writes the stl given a list of vertices. Does not return anything
def createMesh(faces, name):
    name = name.split(".")[0]
    stl_mesh = mesh.Mesh(faces, remove_empty_areas= False) # generates the mesh
    stl_mesh.normals # normalizes the vectors
    print("Saving mesh.")
    stl_mesh.save(settings.OUTPUT_PATH + name + ".stl", mode=stl.Mode.ASCII) # saves the mesh!
    print("Saving complete.")
