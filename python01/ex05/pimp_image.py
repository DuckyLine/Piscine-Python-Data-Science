import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np


def showImage(arr):
    """
    This function could show picture.
    """
    plt.imshow(arr)
    plt.show()


def ft_invert(array) -> np.array:
    """
    Inverts the color of the image received
    """
    for line in array:
        for elem in line:
            elem[0] = 255-elem[0]
            elem[1] = 255-elem[1]
            elem[2] = 255-elem[2]

    return (array)


def ft_red(array) -> np.array:
    """
    This function change colors in red.
    """
    for line in array:
        for elem in line:
            elem[1] = 0
            elem[2] = 0

    return (array)


def ft_green(array) -> np.array:
    """
    This function change colors in green.
    """
    for line in array:
        for elem in line:
            elem[0] = 0
            elem[2] = 0

    return (array)


def ft_blue(array) -> np.array:
    """
    This function change colors in blue.
    """
    for line in array:
        for elem in line:
            elem[0] = 0
            elem[1] = 0

    return (array)


def ft_grey(array) -> np.array:
    """
    This function change colors in grey.
    """
    for line in array:
        for elem in line:
            grey = np.average([elem[0], elem[1], elem[2]], weights=[0.299,0.587,0.114])
            elem[0] = grey
            elem[1] = grey
            elem[2] = grey

    return (array)