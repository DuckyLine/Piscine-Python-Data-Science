import matplotlib.pyplot as plt
from load_image import ft_load
from PIL import Image
import numpy as np
import os


def showImage(arr):
    """
    This function could show picture.
    """
    plt.imshow(arr[:, :, 0:1], cmap="gray")
    plt.show()


def sliceImage(img: Image, y_start: int, y_end: int, x_start: int, x_end: int) -> np.array:
    """
    This function can slice picture.
    """
    arr = np.array(img)[y_start:y_end, x_start:x_end, :]
    return (arr)


def main():
    """
    This function could show the shape of this image and return array of pixels.
    And with slicing the image.
    """
    arr = ft_load("animal.jpeg")

    if arr is None:
        return

    print(f"The shape of image is: {arr.shape}")
    print(arr)

    zoom = sliceImage(arr, 100, 500, 450, 850)[:, :, 0:1]
    print(f"New shape after slicing: {zoom.shape} or {arr[0:400, 0:400, 0].shape}")
    print(zoom)

    showImage(zoom)


if __name__ == "__main__":
    main()