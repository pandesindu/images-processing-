from PIL import Image
from statisticalFilter import *

# morphological operations
# erosion
def Erosion(img_input, coldepth):
    if coldepth == 1:
        img_input = img_input.convert('L')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('L', (horizontalSize, verticalSize))
    pixels_output = img_output.load()

    for i in range(1, horizontalSize - 1):
        for j in range(1, verticalSize - 1):
            min = 255
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if pixels[i + k, j + l] < min:
                        min = pixels[i + k, j + l]
            pixels_output[i, j] = min

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

# dilation
def Dilation(img_input, coldepth):
    if coldepth == 1:
        img_input = img_input.convert('L')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('L', (horizontalSize, verticalSize))
    pixels_output = img_output.load()

    for i in range(1, horizontalSize - 1):
        for j in range(1, verticalSize - 1):
            max = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if pixels[i + k, j + l] > max:
                        max = pixels[i + k, j + l]
            pixels_output[i, j] = max

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

# opening 
def Opening(img_input, coldepth):
    img_output = Erosion(img_input, coldepth)
    img_output = Dilation(img_output, coldepth)
    return img_output

# closing
def Closing(img_input, coldepth):
    img_output = Dilation(img_input, coldepth)
    img_output = Erosion(img_output, coldepth)
    return img_output

#  subtraction of two images
def Subtraction(img_input1, img_input2, coldepth):
    if coldepth == 1:
        img_input1 = img_input1.convert('L')
        img_input2 = img_input2.convert('L')
    
    pixels1 = img_input1.load()
    pixels2 = img_input2.load()
    horizontalSize = img_input1.size[0]
    verticalSize = img_input1.size[1]
    img_output = Image.new('L', (horizontalSize, verticalSize))
    pixels_output = img_output.load()

    for i in range(horizontalSize):
        for j in range(verticalSize):
            pixels_output[i, j] = pixels1[i, j] - pixels2[i, j]

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

# black top hat
def BlackTopHat(img_input, coldepth):
    img_output = Closing(img_input, coldepth)
    img_output = Subtraction(img_output, img_input, coldepth)
    return img_output

# white top hat
def WhiteTopHat(img_input, coldepth):
    img_output = Opening(img_input, coldepth)
    img_output = Subtraction(img_input, img_output, coldepth)
    return img_output


# erotion using a min filter
def ErMinFilter(img_input, coldepth, size):
    if coldepth == 1:
        img_input = img_input.convert('L')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('L', (horizontalSize, verticalSize))
    pixels_output = img_output.load()

    for i in range(size, horizontalSize - size):
        for j in range(size, verticalSize - size):
            min = 255
            for k in range(-size, size + 1):
                for l in range(-size, size + 1):
                    if pixels[i + k, j + l] < min:
                        min = pixels[i + k, j + l]
            pixels_output[i, j] = min

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

# erosion using a max filter 3x3
def ErMaxFilter(img_input, coldepth, size):
    if coldepth == 1:
        img_input = img_input.convert('L')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('L', (horizontalSize, verticalSize))
    pixels_output = img_output.load()

    for i in range(size, horizontalSize - size):
        for j in range(size, verticalSize - size):
            max = 0
            for k in range(-size, size + 1):
                for l in range(-size, size + 1):
                    if pixels[i + k, j + l] > max:
                        max = pixels[i + k, j + l]
            pixels_output[i, j] = max

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
