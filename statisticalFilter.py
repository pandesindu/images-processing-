from PIL import Image, ImageOps 
# median filter with mask size adjustable
def MedianFilter2(img_input, coldepth, maskSize):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(maskSize//2,horizontalSize-maskSize//2):
        for j in range(maskSize//2,verticalSize-maskSize//2):
            r = []
            g = []
            b = []
            for k in range(maskSize):
                for l in range(maskSize):
                    r.append(pixels[i+k-maskSize//2,j+l-maskSize//2][0])
                    g.append(pixels[i+k-maskSize//2,j+l-maskSize//2][1])
                    b.append(pixels[i+k-maskSize//2,j+l-maskSize//2][2])
            r.sort()
            g.sort()
            b.sort()
            newPixels[i,j] = (r[maskSize**2//2],g[maskSize**2//2],b[maskSize**2//2])
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

    # min filter with mask size adjustable
def MinFilter(img_input, coldepth, maskSize):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(maskSize//2,horizontalSize-maskSize//2):
        for j in range(maskSize//2,verticalSize-maskSize//2):
            r = []
            g = []
            b = []
            for k in range(maskSize):
                for l in range(maskSize):
                    r.append(pixels[i+k-maskSize//2,j+l-maskSize//2][0])
                    g.append(pixels[i+k-maskSize//2,j+l-maskSize//2][1])
                    b.append(pixels[i+k-maskSize//2,j+l-maskSize//2][2])
            r.sort()
            g.sort()
            b.sort()
            newPixels[i,j] = (r[0],g[0],b[0])
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

    # max filter with mask size adjustable
def MaxFilter(img_input, coldepth, maskSize):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(maskSize//2,horizontalSize-maskSize//2):
        for j in range(maskSize//2,verticalSize-maskSize//2):
            r = []
            g = []
            b = []
            for k in range(maskSize):
                for l in range(maskSize):
                    r.append(pixels[i+k-maskSize//2,j+l-maskSize//2][0])
                    g.append(pixels[i+k-maskSize//2,j+l-maskSize//2][1])
                    b.append(pixels[i+k-maskSize//2,j+l-maskSize//2][2])
            r.sort()
            g.sort()
            b.sort()
            newPixels[i,j] = (r[-1],g[-1],b[-1])
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

    