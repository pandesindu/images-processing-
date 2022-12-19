from PIL import Image, ImageOps 


# mean filter with mask size adjustable
def MeanFilter2(img_input, coldepth, maskSize):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(maskSize//2,horizontalSize-maskSize//2):
        for j in range(maskSize//2,verticalSize-maskSize//2):
            r = 0
            g = 0
            b = 0
            for k in range(maskSize):
                for l in range(maskSize):
                    r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]
                    g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]
                    b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]
            r //= maskSize**2
            g //= maskSize**2
            b //= maskSize**2
            newPixels[i,j] = (r,g,b)
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

# weighted average filter with mask size adjustable and orthogonal weights is 2, diagonal weights is 1 and the center is 4
def WeightedAverageFilter(img_input, coldepth, maskSize):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(maskSize//2,horizontalSize-maskSize//2):
        for j in range(maskSize//2,verticalSize-maskSize//2):
            r = 0
            g = 0
            b = 0
            for k in range(maskSize):
                for l in range(maskSize):
                    if k==maskSize//2 or l==maskSize//2:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*2
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*2
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*2
                    elif k==maskSize//2 and l==maskSize//2:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*4
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*4
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*4
                    else:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]
            r //= maskSize**2+8
            g //= maskSize**2+8
            b //= maskSize**2+8
            newPixels[i,j] = (r,g,b)
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

