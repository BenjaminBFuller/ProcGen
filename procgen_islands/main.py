import noise
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from PIL import Image
from imageio import imwrite
import random


shape = (800, 800)  # USER OPTIONAL: output size (x,y)
scale = 200         # USER OPTIONAL: higher zoomed in factor = higher number
octaves = 7         # USER OPTIONAL: number of layers; more layers = more detail added
persistence = 0.5   # amplitude that each octave contributes to overall shape
lacunarity = 2.0    # frequency of detail at each octave
seed = np.random.randint(0, 100)

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i / scale,
                                    j / scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity,
                                    repeatx=1024,
                                    repeaty=1024,
                                    base=seed)

blue = [65, 105, 225]
shelf_blue = [115, 141, 223]
green = [34, 139, 34]
dark_green = [15, 150, 0]
dark_green2 = [14, 135, 0]
beach = [238, 214, 175]
beach2 = [238, 205, 149]
snow = [250, 250, 250]
snow2 = [226, 226, 226]
mountain = [139, 137, 137]
mountain2 = [129, 128, 128]


def add_color(world):
    color_world = np.zeros(world.shape + (3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < .05:
                color_world[i][j] = blue
            elif world[i][j] < .075:
                color_world[i][j] = shelf_blue
            elif world[i][j] < .1:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = beach
                else:
                    color_world[i][j] = beach2
            elif world[i][j] < .25:
                rand_int = random.randint(0, 2)
                if rand_int == 0:
                    color_world[i][j] = green
                elif rand_int == 1:
                    color_world[i][j] = dark_green
                else:
                    color_world[i][j] = dark_green2
            elif world[i][j] < .275:
                rand_int = random.randint(0, 4)
                if rand_int == 0:
                    color_world[i][j] = green
                elif rand_int == 1:
                    color_world[i][j] = dark_green
                elif rand_int == 2:
                    color_world[i][j] = dark_green2
                elif rand_int == 3:
                    color_world[i][j] = mountain
                else:
                    color_world[i][j] = mountain2
            elif world[i][j] < 0.35:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = mountain
                else:
                    color_world[i][j] = mountain2
            elif world[i][j] < 0.36:
                rand_int = random.randint(0, 3)
                if rand_int == 0:
                    color_world[i][j] = mountain
                elif rand_int == 1:
                    color_world[i][j] = mountain2
                else:
                    color_world[i][j] = snow2
            elif world[i][j] < .42:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = snow
                else:
                    color_world[i][j] = snow2
            elif world[i][j] < 1.0:
                color_world[i][j] = snow

    return color_world


color_world = add_color(world)
color_world_uint8 = np.uint8(color_world) # lossy conversion without this.
imwrite('islands.png', color_world_uint8)

background = Image.open('islands.png')
my_dpi = 100  # set screen dots per inch

grid = plt.figure(figsize=(float(background.size[0]) / my_dpi, float(background.size[1]) / my_dpi), dpi=my_dpi)
ax = grid.add_subplot(111)

grid.subplots_adjust(left=0, right=1, bottom=0, top=1)

myInterval = 50  # USER OPTIONAL: each grid plot will be (myInterval x myInterval) pixels
a = plticker.MultipleLocator(base=myInterval)
ax.xaxis.set_major_locator(a)
ax.yaxis.set_major_locator(a)

# Adds grid to image with set values
# USER OPTIONAL: linewidth = line thickness
# ax.grid(which='major', axis='both', linestyle='-', color='black', linewidth=1)

ax.imshow(background)

grid.savefig('islands_grid.png', dpi=my_dpi)

im = Image.open('islands_grid.png')
im.show()
