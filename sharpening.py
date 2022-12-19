from PIL import Image, ImageOps 

# gaussian filter 3x3
def GaussianFilter(img_input, coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()

    mask = [[1,2,1],
            [2,4,2],
            [1,2,1]]
    for i in range(1,horizontalSize-1):
        for j in range(1,verticalSize-1):
            r = 0
            g = 0
            b = 0
            for k in range(3):
                for l in range(3):
                    r += pixels[i+k-1,j+l-1][0]*mask[k][l]
                    g += pixels[i+k-1,j+l-1][1]*mask[k][l]
                    b += pixels[i+k-1,j+l-1][2]*mask[k][l]
            newPixels[i,j] = (r//16,g//16,b//16)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output