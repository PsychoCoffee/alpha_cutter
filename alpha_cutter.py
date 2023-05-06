import cv2
import numpy as np
from os import system, name

print("|---------------------|")
print("|     alpha cutter    |")
print("|     by luka beg     |")
print("|      (c) 2023       |")
print("|---------------------|")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def askForLoop():
    a = input("\nDo you wish to continue?\n\n(a)->Yes\n(b)->No\n\nChoice:")
    if(a.lower() == "a"):
        clear()
        loop()
    elif(a.lower() == "b"):
        exit()
    else:
        askForLoop()

def apply_alpha_mask(alpha_image, color_image):
    alpha_image = cv2.resize(alpha_image, (color_image.shape[1], color_image.shape[0]))
    alpha_mask = np.zeros((color_image.shape[0], color_image.shape[1], 1), dtype=np.uint8)
    alpha_mask[:, :, 0] = alpha_image
    b, g, r = cv2.split(color_image)
    masked_color_image = cv2.merge((b, g, r, alpha_mask))
    return masked_color_image

def loop():
    color_image_path = input("Color img: ")
    alpha_image_path = input("Alpha img: ")
    alpha_image = cv2.imread(alpha_image_path, cv2.IMREAD_GRAYSCALE)
    color_image = cv2.imread(color_image_path, cv2.IMREAD_COLOR)
    result = apply_alpha_mask(alpha_image, color_image)
    output_file_path = color_image_path + "_"
    cv2.imwrite(output_file_path + ".png", result)

    print("Successful")
    
    askForLoop()

def main():
    loop()

if __name__ == '__main__':
    main()
