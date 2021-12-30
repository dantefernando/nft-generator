import numpy as np
import random
import os
import time
from PIL import Image, ImageOps

from colorGenerators import *


def rarity_display(rarity_count):
    """
    Procedure used to display how many images/ducks of each rarity was generated
    """

    for key in rarity_count:
        print(f"{key}:{rarity_count[key]}")


def addRarity(rarity_count, rarity):
    """
    Keep count of the quantity of images
    for each rarity.
    """

    # Rarity hasn't been added yet to the dict
    if rarity not in rarity_count:

        # Set key to rarity name and set value to value
        rarity_count[rarity] = 1

    else:  # Rarity is in the dict

        # Add 1 to the rarity's key's value
        rarity_count[rarity] += 1

    return rarity_count


def img_generator(rarity, christmas_data, data, i, PATH, PF, EW, EC, BC, OT, BG, BK, CH):
    """
    Generates image with the specified colors?
    """

    RGB_data = []

    # makes a new array replacing the letters with the generated RGB colors
    if rarity == 'holiday':
        for j in range(30):
            for k in range(30):
                if christmas_data[j][k] == 'PF':
                    RGB_data.append(PF)
                elif christmas_data[j][k] == 'EW':
                    RGB_data.append(EW)
                elif christmas_data[j][k] == 'EC':
                    RGB_data.append(EC)
                elif christmas_data[j][k] == 'BC':
                    RGB_data.append(BC)
                elif christmas_data[j][k] == 'OT':
                    RGB_data.append(OT)
                elif christmas_data[j][k] == 'BG':
                    RGB_data.append(BG)
                elif christmas_data[j][k] == 'BK':
                    RGB_data.append(BK)
                elif christmas_data[j][k] == 'CH':
                    RGB_data.append(CH)
    else:
        for j in range(30):
            for k in range(30):
                if data[j][k] == 'PF':
                    RGB_data.append(PF)
                elif data[j][k] == 'EW':
                    RGB_data.append(EW)
                elif data[j][k] == 'EC':
                    RGB_data.append(EC)
                elif data[j][k] == 'BC':
                    RGB_data.append(BC)
                elif data[j][k] == 'OT':
                    RGB_data.append(OT)
                elif data[j][k] == 'BG':
                    RGB_data.append(BG)
                elif data[j][k] == 'BK':
                    RGB_data.append(BK)


    # new dimensions for image
    dimensions = 480,480

    # array handling with numpy
    RGB_data = np.array(RGB_data, dtype=np.uint8)
    RGB_data = RGB_data.reshape(30,30,3)

    # using PIL to turn the RGB values into an image
    img_data = Image.fromarray(RGB_data, 'RGB')
    img_data = img_data.resize(dimensions, resample=0)
    # img_data.show()

    # flips image if its upside down rarity
    if rarity == 'upside down':
        img_data = ImageOps.flip(img_data)

    img_data.save(f'{PATH}/duck-{i+1}.png')



def getRarity():
    """
    Generates different Rarities
    """

    number = random.randint(1, 10000)

    # 50% chance of getting this rarity
    if number >= 1 and number <= 5000:
        rarity = 'common'
        PF, EW, EC, BC, OT, BG, BK, CH = common()

    # # 25% chance of getting this rarity
    # elif number >= 5000 and number <= 7500:
    #     rarity = 'uncommon'
    #     uncommon()

    # 15% chance of getting this rarity

    elif number >= 7500 and number <= 9000:
        rarity = 'rare'
        PF, EW, EC, BC, OT, BG, BK, CH = rare()

    # 2% chance of getting this rarity
    elif number >= 9000 and number <= 9200:
        rarity = 'legendary'
        main_colors = 'red'
        PF, EW, EC, BC, OT, BG, BK, CH = legendary_r()

    # 2% chance of getting this rarity
    elif number >= 9200 and number <= 9400:
        rarity = 'legendary'
        main_colors = 'green'
        PF, EW, EC, BC, OT, BG, BK, CH = legendary_g()

    # 2% chance of getting this rarity
    elif number >= 9400 and number <= 9600:
        rarity = 'legendary'
        main_colors = 'blue'
        PF, EW, EC, BC, OT, BG, BK, CH = legendary_b()

    # 1% chance of getting this rarity
    elif number >= 9600 and number <= 9700:
        rarity = 'classified'
        main_colors = 'black'
        PF, EW, EC, BC, OT, BG, BK, CH = classified_blk()

    # 1% chance of getting this rarity
    elif number >= 9700 and number <= 9800:
        rarity = 'classified'
        main_colors = 'white'
        PF, EW, EC, BC, OT, BG, BK, CH = classified_wht()

    # 0.1% chance of getting this rarity
    elif number >= 9700 and number <= 9710:
        rarity = 'holiday'
        main_colors = 'christmas'
        PF, EW, EC, BC, OT, BG, BK, CH = holiday_christmas()

    # 0.01% chance of getting this rarity
    elif number == 10000:
        rarity = 'upside down'
        PF, EW, EC, BC, OT, BG, BK, CH = upsidedown()

    # this is here until all 10000 numbers are occupied by a rarity
    else:
        rarity = 'common'
        PF, EW, EC, BC, OT, BG, BK, CH = common()

    return rarity, PF, EW, EC, BC, OT, BG, BK, CH


def getNumImages():
    """
    Get Number of images to generate from user
    """

    while True:
        try:
            numImages = int(input('How many images would you like to generate?: '))
            if numImages < 1:  # User entered value less than 1
                print("Number of images must be at least 1.")
            else:  # Value is an integer and greater than or equal to 1
                break
        except ValueError:
            print('Wrong input...')
    return numImages


def fileData():
    """
    Reads file data from stored files?

    Returns: list of file data for pixels

    """

    # Turns image_data file into a list
    with open('image-data-files/image_data.txt', 'r') as file:
        # New array that contains all RGB pixel values
        data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()] # made by Royce Chan

    # Turns christmas_image_data file into a list
    with open('image-data-files/image_data_christmas.txt', 'r') as christmas_file:
        # New array that contains all RGB pixel values
        christmas_data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in christmas_file.readlines()] # also made by Royce Chan

    return data, christmas_data


def mkImagesDir():
    """
    Creates Images/ directory to save generated images

    Returns: path of Images/ dir to store images
    """

    cwd = os.getcwd()
    path = os.path.join(cwd, "Images")

    # Try and make the image/ dir assuming it doesn't exist
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    return path


def main():
    """
    Main Function
    """

    # Make the Images/ dir
    PATH = mkImagesDir()

    # Array used to display rarities - can be seen in last procedure
    rarity_count = {}

    rarity_count = {
        "common": 0,
        "uncommon": 0,
        "rare": 0,
        "legendary": 0,
        "classified": 0,
        "christmas": 0,
        "upside down": 0
                    }

    # Return file data of images
    data, christmas_data = fileData()

    # Asks user how many images they want to make
    numImages = getNumImages()

    # Start time for counting elapsed image generation time
    start_time = time.time()

    # Loop to generate images
    for i in range(0, numImages):
        rarity, PF, EW, EC, BC, OT, BG, BK, CH = getRarity()
        img_generator(rarity, christmas_data, data, i, PATH, PF, EW, EC, BC, OT, BG, BK, CH)

        rarity_count = addRarity(rarity_count, rarity)


    # Prints elapsed time to generate images rounded to 2 decimal places
    print(f"Process finished --- {round(time.time()-start_time, 2)}s seconds ---")
    rarity_display(rarity_count)


if __name__ == '__main__':
    main()

