from PIL import Image, ImageOps
from processing_list import * 
# laplacian filter with mask size adjustable
def LaplacianFilter(img_input, coldepth, maskSize):
    if coldepth!=24:
        img_input=PixelReplication(img_input, coldepth)
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()

    kernel = [[0,1,0],[1,-4,1],[0,1,0]]

    for i in range(maskSize//2,horizontalSize-maskSize//2):
        for j in range(maskSize//2,verticalSize-maskSize//2):
            r = 0
            g = 0
            b = 0
            for k in range(maskSize):
                for l in range(maskSize):
                    if k==0 and l==0:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*kernel[k][l]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*kernel[k][l]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*kernel[k][l]
                    elif k==0 and l==1:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*kernel[k][l]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*kernel[k][l]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*kernel[k][l]
                    elif k==0 and l==2:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*kernel[k][l]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*kernel[k][l]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*kernel[k][l]
                    elif k==2 and l==0:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*kernel[k][l]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*kernel[k][l]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*kernel[k][l]
                    elif k==2 and l==1:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*kernel[k][l]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*kernel[k][l]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*kernel[k][l]
                    elif k==2 and l==2:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*kernel[k][l]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*kernel[k][l]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*kernel[k][l]
                    elif k==1 and l==0:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*kernel[k][l]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*kernel[k][l]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*kernel[k][l]
                    elif k==1 and l==2:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*kernel[k][l]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*kernel[k][l]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*kernel[k][l]
                    elif k==1 and l==1:
                        r += pixels[i+k-maskSize//2,j+l-maskSize//2][0]*kernel[k][l]
                        g += pixels[i+k-maskSize//2,j+l-maskSize//2][1]*kernel[k][l]
                        b += pixels[i+k-maskSize//2,j+l-maskSize//2][2]*kernel[k][l]
            if r<0:
                r=0
            if g<0:
                g=0
            if b<0:
                b=0
            if r>255:
                r=255
            if g>255:
                g=255
            if b>255:
                b=255
            newPixels[i,j] = (r,g,b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# first gradient filter
def FirstGradientFilter(img_input, coldepth) : 
    if coldepth != 24 :
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    for i in range(horizontalSize-1) :
        for j in range(verticalSize-1) :
            r,g,b = pixels[i,j]
            r2,g2,b2 = pixels[i+1,j]
            r3,g3,b3 = pixels[i,j+1]
            rx = (r*-1)+(r2*1)
            gx = (g*-1)+(g2*1)
            bx = (b*-1)+(b2*1)

            ry = (r*-1)+(r3*1)
            gy = (g*-1)+(g3*1)
            by = (b*-1)+(b3*1)
            rxy = (abs(rx))+(abs(ry))
            gxy = (abs(gx))+(abs(gy))
            bxy = (abs(bx))+(abs(by))
            newPixels[i,j] = (rxy,gxy,bxy)

    if coldepth == 1 :
        img_output = img_output.convert("1")
    elif coldepth == 8 :
        img_output = img_output.convert("L")
    else :
        img_output = img_output.convert("RGB")

    return img_output

# center difference filter
def CenterDifferenceFilter(img_input, coldepth) :
    if coldepth != 24 :
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    mask = [-1,0,1]
    for i in range(1,horizontalSize-1) :
        for j in range(1,verticalSize-1) :
            r,g,b = pixels[i,j]
            r2,g2,b2 = pixels[i+1,j] # right
            r3,g3,b3 = pixels[i-1,j] # left
            r4,g4,b4 = pixels[i,j+1] # up
            r5,g5,b5 = pixels[i,j-1] # down
            
            rx = (r3*mask[0])+(r2*mask[2])
            gx = (g3*mask[0])+(g2*mask[2])
            bx = (b3*mask[0])+(b2*mask[2])

            ry = (r5*mask[0])+(r4*mask[2])
            gy = (g5*mask[0])+(g4*mask[2])
            by = (b5*mask[0])+(b4*mask[2])

            rxy = (abs(rx))+(abs(ry))
            gxy = (abs(gx))+(abs(gy))
            bxy = (abs(bx))+(abs(by))
            newPixels[i,j] = (rxy,gxy,bxy)


    if coldepth == 1 :
        img_output = img_output.convert("1")
    elif coldepth == 8 :
        img_output = img_output.convert("L")
    else :
        img_output = img_output.convert("RGB")

    return img_output

# sobel filter
def SobelFilter(img_input, coldepth) :
    if coldepth != 24 :
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    sx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    sy = [[-1,-2,-1],[0,0,0],[1,2,1]]
    offset = len(sx)//2

    for i in range(offset,horizontalSize-offset) :
        for j in range(offset,verticalSize-offset) :
            xRGB = [0,0,0]
            yRGB = [0,0,0]
            for k in range(len(sx)) :
                for l in range(len(sx)) :
                    r,g,b = pixels[i+k-offset,j+l-offset]
                    xRGB[0] += r*sx[k][l]
                    xRGB[1] += g*sx[k][l]
                    xRGB[2] += b*sx[k][l]

                    yRGB[0] += r*sy[k][l]
                    yRGB[1] += g*sy[k][l]
                    yRGB[2] += b*sy[k][l]

            for k in range(len(xRGB)) :
                xRGB[k] = abs(xRGB[k])
                yRGB[k] = abs(yRGB[k])
            
            newPixels[i,j] = (xRGB[0]+yRGB[0],xRGB[1]+yRGB[1],xRGB[2]+yRGB[2])
            
    if coldepth == 1 :
        img_output = img_output.convert("1")
    elif coldepth == 8 :
        img_output = img_output.convert("L")
    else :
        img_output = img_output.convert("RGB")

    return img_output

# prewitt filter
def PrewittFilter(img_input, coldepth) :
    if coldepth != 24 :
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    sx = [[-1,0,1],[-1,0,1],[-1,0,1]]
    sy = [[-1,-1,-1],[0,0,0],[1,1,1]]
    offset = len(sx)//2

    for i in range(offset,horizontalSize-offset) :
        for j in range(offset,verticalSize-offset) :
            xRGB = [0,0,0]
            yRGB = [0,0,0]
            for k in range(len(sx)) :
                for l in range(len(sx)) :
                    r,g,b = pixels[i+k-offset,j+l-offset]
                    xRGB[0] += r*sx[k][l]
                    xRGB[1] += g*sx[k][l]
                    xRGB[2] += b*sx[k][l]

                    yRGB[0] += r*sy[k][l]
                    yRGB[1] += g*sy[k][l]
                    yRGB[2] += b*sy[k][l]

            for k in range(len(xRGB)) :
                xRGB[k] = abs(xRGB[k])
                yRGB[k] = abs(yRGB[k])
            
            newPixels[i,j] = (xRGB[0]+yRGB[0],xRGB[1]+yRGB[1],xRGB[2]+yRGB[2])
            
    if coldepth == 1 :
        img_output = img_output.convert("1")
    elif coldepth == 8 :
        img_output = img_output.convert("L")
    else :
        img_output = img_output.convert("RGB")

    return img_output

# roberts filter
def RobertsFilter(img_input, coldepth) :
    if coldepth != 24 :
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    sx = [[0,1],[-1,0]]
    sy = [[1,0],[0,-1]]
    offset = len(sx)//2

    for i in range(offset,horizontalSize-offset) :
        for j in range(offset,verticalSize-offset) :
            xRGB = [0,0,0]
            yRGB = [0,0,0]
            for k in range(len(sx)) :
                for l in range(len(sx)) :
                    r,g,b = pixels[i+k-offset,j+l-offset]
                    xRGB[0] += r*sx[k][l]
                    xRGB[1] += g*sx[k][l]
                    xRGB[2] += b*sx[k][l]

                    yRGB[0] += r*sy[k][l]
                    yRGB[1] += g*sy[k][l]
                    yRGB[2] += b*sy[k][l]

            for k in range(len(xRGB)) :
                xRGB[k] = abs(xRGB[k])
                yRGB[k] = abs(yRGB[k])
            
            newPixels[i,j] = (xRGB[0]+yRGB[0],xRGB[1]+yRGB[1],xRGB[2]+yRGB[2])
            
    if coldepth == 1 :
        img_output = img_output.convert("1")
    elif coldepth == 8 :
        img_output = img_output.convert("L")
    else :
        img_output = img_output.convert("RGB")

    return img_output

# roberts filter direction x
def RobertsFilterX(img_input, coldepth) :
    if coldepth != 24 :
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    sx = [[0,1],[-1,0]]
    offset = len(sx)//2

    for i in range(offset,horizontalSize-offset) :
        for j in range(offset,verticalSize-offset) :
            xRGB = [0,0,0]
            for k in range(len(sx)) :
                for l in range(len(sx)) :
                    r,g,b = pixels[i+k-offset,j+l-offset]
                    xRGB[0] += r*sx[k][l]
                    xRGB[1] += g*sx[k][l]
                    xRGB[2] += b*sx[k][l]

            for k in range(len(xRGB)) :
                xRGB[k] = abs(xRGB[k])
            
            newPixels[i,j] = (xRGB[0],xRGB[1],xRGB[2])
            
    if coldepth == 1 :
        img_output = img_output.convert("1")
    elif coldepth == 8 :
        img_output = img_output.convert("L")
    else :
        img_output = img_output.convert("RGB")

    return img_output

# compass filter
def CompassFilter(img_input, coldepth) :
    if coldepth != 24 :
        img_input = img_input.convert('RGB')
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    sx = [[-1,0,1],[-1,0,1],[-1,0,1]]
    sy = [[-1,-1,-1],[0,0,0],[1,1,1]]
    offset = len(sx)//2

    for i in range(offset,horizontalSize-offset) :
        for j in range(offset,verticalSize-offset) :
            xRGB = [0,0,0]
            yRGB = [0,0,0]
            for k in range(len(sx)) :
                for l in range(len(sx)) :
                    r,g,b = pixels[i+k-offset,j+l-offset]
                    xRGB[0] += r*sx[k][l]
                    xRGB[1] += g*sx[k][l]
                    xRGB[2] += b*sx[k][l]

                    yRGB[0] += r*sy[k][l]
                    yRGB[1] += g*sy[k][l]
                    yRGB[2] += b*sy[k][l]

            for k in range(len(xRGB)) :
                xRGB[k] = abs(xRGB[k])
                yRGB[k] = abs(yRGB[k])
            
            newPixels[i,j] = (xRGB[0]+yRGB[0],xRGB[1]+yRGB[1],xRGB[2]+yRGB[2])
            
    if coldepth == 1 :
        img_output = img_output.convert("1")
    elif coldepth == 8 :
        img_output = img_output.convert("L")
    else :
        img_output = img_output.convert("RGB")

    return img_output