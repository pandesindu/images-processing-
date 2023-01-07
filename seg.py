from PIL import Image

# funtion for segmentation
def Segmentation(img_input, coldepth):
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

    # funtion for segmentation image with threshold
def SegmentationThreshold(img_input, coldepth, threshold):
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
            if max > threshold:
                pixels_output[i, j] = 255
            else:
                pixels_output[i, j] = 0

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

# funtion for segmentation image using edge detection
def SegmentationEdgeDetection(img_input, coldepth):
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
            if max > 0:
                pixels_output[i, j] = 255
            else:
                pixels_output[i, j] = 0

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output