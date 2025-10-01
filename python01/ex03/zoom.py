from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt


def showImage(zoom):
    """
    This function could show picture.
    """
    plt.imshow(zoom[:, :, 0], cmap="gray")
    plt.show()



def main():
    """
    This function could show the shape of this image and return array of pixels.
    And with slicing the image.
    """
    img_path = "animal.jpeg"

    if not os.path.exists(img_path):
        print(f"ERROR: The path of image '{img_path}' doesn't exist !")
        return
    
    img = Image.open(img_path)
    img_rgb = img.convert("RGB")

    arr = np.array(img_rgb)
    print(f"The shape of image is: {arr.shape}")
    print(arr)

    zoom = arr[100:500, 450:850, 0:1]
    print(f"New shape after slicing: {zoom.shape} or {arr[0:400, 0:400, 0].shape}")
    print(zoom)

    showImage(zoom)


if __name__ == "__main__":
    main()