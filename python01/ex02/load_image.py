from PIL import Image
import os


def ft_load(path: str) -> list:

    if not os.path.exists(path):
        print(f"ERROR: The path of image '{path}' doesn't exist !")
        return
    
    img = Image.open(path)

    if img.format not in ["JPG", "JPEG"]:
        print(f"ERROR: The format of image is {img.format}, but the format require is JPG or JPEG")
        return
    
    print(f"The shape of image is: ({img.width}, {img.height}, {len(img.mode)})")
    
    img_rgb = img.convert("RGB")
    pixels = list(img.getdata())

    return (pixels)