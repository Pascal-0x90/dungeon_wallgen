import json
import random

# fill -4206 11 1836 -4208 13 1836 minecraft:stone_bricks replace minecraft:air
# fill -4206 11 1836 -4208 13 1836 minecraft:air replace minecraft:stone_bricks
# /fill   x  y   z     x   y   z
MIN_Y = 11
MAX_Y = 13

MAX_X = 4257
MIN_X = 4145
MAX_Z = -1936
MIN_Z = -1808

VOID_MIN_X = 4184
VOID_MAX_X = 4212
VOID_MAX_Z = -1865
VOID_MIN_Z = -1892

walls = []

def write_to_file(x,z,flag,strang): # int,int,string,string
    fp = open(".\data\\wallgen\\functions\\" + str(x*-1) + "_" + str(z*-1) + "_" + flag + ".mcfunction", "w")
    fp.write(strang)
    fp.close()

def gen_wall(x,z):
    # Define file
    if (z+4) <= MIN_Z:
        wall = "fill -"+ str(x) + " " + str(11) + " " + str(-1*z-1) + " -" + str(x) + " " + str(13)  + " " + str(-1*z-3) + " " + "minecraft:stone_bricks replace minecraft:air"
        air = "fill -"+ str(x) + " " + str(11) + " " + str(-1*z-1) + " -" + str(x) + " " + str(13)  + " " + str(-1*z-3) + " " + "minecraft:air replace minecraft:stone_bricks"
        # wallgen:<command>
        walls.append(["wallgen:" + str(x*-1) + "_" + str((z-3)*-1) + "_" + "wall", "wallgen:" + str(x*-1) + "_" + str((z-3)*-1) + "_" + "air" ])
        write_to_file(x,z-3,"wall",wall)
        write_to_file(x,z-3,"air",air)
    if (x+4) <= MAX_X:
        # wallgen:<command>
        walls.append(["wallgen:" + str((x+3)*-1) + "_" + str(z*-1) + "_" + "wall", "wallgen:" + str((x+3)*-1) + "_" + str(z*-1) + "_" + "air" ])
        wall = "fill -"+ str(x+1) + " " + str(11) + " " + str(-1*z) + " -" + str(x+3) + " " + str(13)  + " " + str(-1*z) + " " + "minecraft:stone_bricks replace minecraft:air"
        air = "fill -"+ str(x+1) + " " + str(11) + " " + str(-1*z) + " -" + str(x+3) + " " + str(13)  + " " + str(-1*z) + " " + "minecraft:air replace minecraft:stone_bricks"
        write_to_file(x+3,z,"wall",wall)
        write_to_file(x+3,z,"air",air)

for x in range(MIN_X,MAX_X+4,4):
    for z in range(MAX_Z,MIN_Z+4,4):
        if not (x >= VOID_MIN_X and x <= VOID_MAX_X) or not (z >= VOID_MIN_Z and z <= VOID_MAX_Z):
            gen_wall(x,z)

# Make the random things
sets = ["a","b","c","d","e","f","g","h"]
seen = []
for i in range(8):
    on = {}
    off = {}
    on["values"] = []
    off["values"] = []
    for _ in range(477):
        idx = random.randint(0,len(walls)-1)
        while idx in seen:
            idx = random.randint(0,len(walls)-1)
        on["values"].append(walls[idx][0])
        off["values"].append(walls[idx][1])
    with open(".\\data\\wallgen\\tags\\functions\\set" + sets[i] + "_on.json", "w") as fp:
        json.dump(on, fp, indent=2)
    with open(".\\data\\wallgen\\tags\\functions\\set" + sets[i] + "_off.json", "w") as fp:
        json.dump(off, fp, indent=2)
