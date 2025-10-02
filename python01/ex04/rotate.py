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


def loadImage(path: str) -> Image:
    """
    This function can load and return Image.
    """
    if not os.path.exists(path):
        print(f"ERROR: The path of image '{path}' doesn't exist !")
        return
    
    img = Image.open(path)

    if img.format not in ["JPG", "JPEG"]:
        print(f"ERROR: The format of image is {img.format}, but the format require is JPG or JPEG")
        return
    
    img_rgb = img.convert("RGB")
    return (img_rgb)


def transpose(arr: np.array) -> np.array:
    """
    This function can transpose array.
    """
    H, W, C = arr.shape
    new_arr = np.zeros((W, H, C), dtype=arr.dtype)

    for i in range(H):
        for j in range(W):
            new_arr[j, i, :] = arr[i, j, :]

    return (new_arr)


def main():
    arr = ft_load("animal.jpeg")

    if arr is None:
        return

    slice = sliceImage(arr, 100, 500, 450, 850)[:, :, 0:1]
    print(f"The shape of image is: {slice.shape} or {slice[0:400, 0:400, 0].shape}")
    print(slice)

    arr_transposed = transpose(slice)
    print(f"New shape after Transpose: {slice[0:400, 0:400, 0].shape}")
    print(arr_transposed[:, :, 0])

    showImage(arr_transposed)


if __name__ == "__main__":
    main()