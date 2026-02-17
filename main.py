#!/usr/bin/env python3
from PIL import Image
import numpy as np

img = Image.open('pic-name-here.jpg/png/etc.')
max_size = (250, 250) 
img.thumbnail(max_size)
width, height = img.size
print(f"Successfully loaded image.\nImage size: {height} x {width}")

pixels = list(img.getdata())

pixels_matrix = []
for i in range(height):
    pixels_list = []
    for j in range(width):
        index = i*width + j
        pixels_list.append(pixels[index])
    pixels_matrix.append(pixels_list)

for i in range(height):
    for j in range(width):
        avg = (pixels_matrix[i][j][0] + pixels_matrix[i][j][1] + pixels_matrix[i][j][2])/3
        pixels_matrix[i][j] = avg

char = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
char_len = len(char)

ascii_art = []
for i in range(height):
    ascii_row = []
    for j in range(width):
        pixel_value = pixels_matrix[i][j]
        index = int(pixel_value*(char_len - 1)/255)
        ascii_row.append(char[index])
    ascii_art.append(''.join(x*2 for x in ascii_row))
    
for row in ascii_art:
    print(row)