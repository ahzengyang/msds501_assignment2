# DO NOT ADD ANY OTHER PACKAGES AND LIBRARIES


def create_image_array(file_name):
    """
    Create a function called create_image_array() which takes
    file_name as an input variable and returns a list
    with the given width and height.
    """
    rgb = list()
    with open(file_name) as f:
        img_width = int(f.readline()) # hor len
        img_height = int(f.readline()) # vert len
        for h in range(img_height):
            rgb.insert(h, list())
            for _ in range(img_width):
                rgb[h].append([int(x) for x in f.readline().split(",")])
    return rgb
        


def xray_filter(numbers):
    """
    Create xray_filter() that takes a list and returns a new list.
    This new list includes updated r,g,b values that
    r_value = 255 - r_value
    g_value = 255 - g_value
    and b_value = 255 – b_value.
    """
    return [[[255 - v for v in numbers[h][w]] for w in range(len(numbers[h]))] for h in range(len(numbers))]


def adjust_r_g_b(numbers, r_ratio, g_ratio, b_ratio):
    """
    Create a function called adjust_r_g_b() that takes the image array and
    three float values that are multiplied to r,g, and b values accordingly.
    The adjusted value should be rounded to an integer.
    """
    for h in range(len(numbers)):
        for w in range(len(numbers[h])):
            numbers[h][w] = [round(o * a) for o, a in zip(numbers[h][w], [r_ratio, g_ratio, b_ratio])]
    return numbers


def upside_down(numbers):
    """
    Create a function called upside_down() that takes a list and
    reverses the list.
    """
    numbers.reverse()
    return numbers


def vertical_flip(numbers):
    """
    Create a function called vertical_flip() that
    takes a list and returns a list
    where values in each row are vertically flipped.
    """
    for h in range(len(numbers)):
        numbers[h].reverse()
    return numbers


def create_border(**kargs):
    """
    Add a border around the images with given
    red, green, blue and pixel values.
    Input parameters are given as arbitary keyword arguments
    including numbers, red, green, blue and pixel.
    "numbers" is a list of pixel values of the input image created
    by create_image_array().
    "red", "green", "blue" are indicating values for rgb values.
    The "pixel" number of [red, green, blue] value should be added
    at the beginning and end of each row.
    In addition, the returned list should have
    the "pixel" number of rows only consists
    with the given red, green, blue at the beginning and end of "numbers".
    """
    img = kargs.get("numbers")
    if img == None: # exit if img array not provided
        return
    rgb = [kargs.get("red", 128), kargs.get("green", 0), kargs.get("blue", 128)] # purple default
    border_len = kargs.get("pixel", 1)
    for h in range(len(img)): # add L/R border
        for i in range(border_len):
            img[h].insert(0, rgb)
            img[h].append(rgb)
    border = [rgb for _ in range(len(img[0]))] # add T/B border
    for i in range(border_len):
        img.insert(i, border)
        img.append(border)
    return img