from assignment2 import *
import pickle

def load_pickle_file(file_name):
    """
    Create a function called load_pickle_file() which takes a pickle file
    called file_name as an input variable, and returned its python object.
    """
    with open(file_name, "rb") as file:
        return pickle.load(file)

def test_create_image_array_1():
    file_name = 'data/curly.txt'
    pickle_file_name = 'output/curly/pickle/create_image_array.pickle'
    assert create_image_array(file_name) ==\
           load_pickle_file(pickle_file_name)


def test_xray_filter_1():
    file_name = 'data/curly.txt'
    pickle_file_name = 'output/curly/pickle/xray_filter.pickle'
    assert xray_filter(create_image_array(file_name)) ==\
           load_pickle_file(pickle_file_name)


def test_adjust_r_g_b_1():
    file_name = 'data/curly.txt'
    pickle_file_name = 'output/curly/pickle/adjust_r_g_b.pickle'
    r_ratio = 0.9
    g_ratio = 0
    b_ratio = 0.8

    assert adjust_r_g_b(create_image_array(file_name),
                        r_ratio, g_ratio, b_ratio) ==\
           load_pickle_file(pickle_file_name)


def test_upside_down_1():
    file_name = 'data/curly.txt'
    pickle_file_name = 'output/curly/pickle/upside_down.pickle'
    assert upside_down(create_image_array(file_name)) ==\
           load_pickle_file(pickle_file_name)


def test_vertical_flip_1():
    file_name = 'data/curly.txt'
    pickle_file_name = 'output/curly/pickle/vertical_flip.pickle'
    assert vertical_flip(create_image_array(file_name)) ==\
           load_pickle_file(pickle_file_name)


def test_create_border_1():
    file_name = 'data/curly.txt'
    pickle_file_name = 'output/curly/pickle/create_border.pickle'
    r = 120
    g = 220
    b = 120
    pixel = 20
    assert create_border(numbers=create_image_array(file_name),
                         red=r,
                         green=g,
                         blue=b,
                         pixel=pixel) ==\
           load_pickle_file(pickle_file_name)


def test_create_image_array_2():
    file_name = 'data/siamese.txt'
    pickle_file_name = 'output/siamese/pickle/create_image_array.pickle'
    assert create_image_array(file_name) ==\
           load_pickle_file(pickle_file_name)


def test_xray_filter_2():
    file_name = 'data/siamese.txt'
    pickle_file_name = 'output/siamese/pickle/xray_filter.pickle'
    assert xray_filter(create_image_array(file_name)) ==\
           load_pickle_file(pickle_file_name)


def test_adjust_r_g_b_2():
    file_name = 'data/siamese.txt'
    pickle_file_name = 'output/siamese/pickle/adjust_r_g_b.pickle'
    r_ratio = 0
    g_ratio = 0.8
    b_ratio = 0.7
    assert adjust_r_g_b(create_image_array(file_name),
                        r_ratio, g_ratio, b_ratio) ==\
           load_pickle_file(pickle_file_name)


def test_upside_down_2():
    file_name = 'data/siamese.txt'
    pickle_file_name = 'output/siamese/pickle/upside_down.pickle'
    assert upside_down(create_image_array(file_name)) ==\
           load_pickle_file(pickle_file_name)


def test_vertical_flip_2():
    file_name = 'data/siamese.txt'
    pickle_file_name = 'output/siamese/pickle/vertical_flip.pickle'
    assert vertical_flip(create_image_array(file_name)) ==\
           load_pickle_file(pickle_file_name)


def test_create_border_2():
    file_name = 'data/siamese.txt'
    pickle_file_name = 'output/siamese/pickle/create_border.pickle'
    r = 255
    g = 100
    b = 180
    pixel = 10
    assert create_border(numbers=create_image_array(file_name),
                         red=r,
                         green=g,
                         blue=b,
                         pixel=pixel) ==\
           load_pickle_file(pickle_file_name)

# Custom Unit Tests
def test_create_img_arr():
    assert create_image_array("test.txt") == [[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]]

def test_copy_img():
    assert copy_image(create_image_array("test.txt")) == [[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]]

def test_upside_down_custom():
    assert upside_down([[[1,2,3],[5,6,7],[9,10,11]],  
                        [[11,12,13],[15,16,17],[19,20,21]]]) == [[[11, 12, 13], [15, 16, 17], [19, 20, 21]],
                                                                 [[1, 2, 3], [5, 6, 7], [9, 10, 11]]]
