from PIL import Image, ImageOps 
# UTS 
def ImgCircleAndDiamond(img_input,coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')

    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            if (i-horizontalSize//2)**2+(j-verticalSize//2)**2 < (horizontalSize//2)**2:
                newPixels[i, j] = (255-r,255-g, 255-b)
                r, g, b = pixels[i, j]
                if abs(i-horizontalSize//2)+abs(j-verticalSize//2) < horizontalSize//2:
                    newPixels[i, j] = (r,g,b)
            else:
                newPixels[i, j] = (r, g, b)
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

def BonusUts(img_input, coldepth):
    # solusi 1
    # img_output=ImageOps.invert(img_input)
    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    pixelss = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    pixels = img_output.load()

    # make a variable to store the radius of the image
    radiusX = img_input.size[0]//2
    radiusY = img_input.size[1]//2

    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixelss[i, j]

            if i+j <= verticalSize:
                if i < j:
                    pixels[i, j] = (255-r, 255-g, 255-b)
                    # pixels[i, j] = (255-r, 255-g, 255-b)
                    if (i-horizontalSize//2)**2/radiusX**2 + (j-verticalSize//2)**2/radiusY**2 <= 1:
                        r, g, b = pixelss[i, j]
                        pixels[i, j] = (r, g, b)
                        if abs(i - horizontalSize//2) + abs(j - verticalSize//2) < horizontalSize//2:
                            
                            pixels[i, j] = (255-r, 255-g, 255-b)
                    else:
                        pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (r, g, b)
                    if (i-horizontalSize//2)**2/radiusX**2 + (j-verticalSize//2)**2/radiusY**2 <= 1:
                        r, g, b = pixelss[i, j]
                        pixels[i, j] = (255-r, 255-g, 255-b)
                        if abs(i - horizontalSize//2) + abs(j - verticalSize//2) < horizontalSize//2:
                        
                            pixels[i, j] = (r, g, b)
                    else:
                        pixels[i, j] = (r, g, b)

            elif i > j:
                pixels[i, j] = (255-r, 255-g, 255-b)
                if (i-horizontalSize//2)**2/radiusX**2 + (j-verticalSize//2)**2/radiusY**2 <= 1:
                    r, g, b = pixelss[i, j]
                    pixels[i, j] = (r, g, b)
                    if abs(i - horizontalSize//2) + abs(j - verticalSize//2) < horizontalSize//2:
                    
                        pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (255-r, 255-g, 255-b)

            else:
                pixels[i, j] = (r, g, b)
                if (i-horizontalSize//2)**2/radiusX**2 + (j-verticalSize//2)**2/radiusY**2 <= 1:
                    r, g, b = pixelss[i, j]
                    pixels[i, j] = (255-r, 255-g, 255-b)
                    if abs(i - horizontalSize//2) + abs(j - verticalSize//2) < horizontalSize//2:
                        pixels[i, j] = (r, g, b)
                else:
                    pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
