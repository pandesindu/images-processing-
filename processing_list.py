import math
# import re
from PIL import Image, ImageOps 

# pointwise operation
# negatif Image
def ImgNegative(img_input,coldepth): 
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 
 
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1])) 
    pixels = img_output.load() 
    for i in range(img_output.size[0]): 
        for j in range(img_output.size[1]): 
            r, g, b = img_input.getpixel((i, j)) 
            pixels[i,j] = (255-r, 255-g, 255-b) 
 
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB") 

    return img_output


# rotate 90 derajat
def ImgRotate(img_input,coldepth,direction): 
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 
    
    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
    pixels = img_output.load() 
    for i in range(img_output.size[0]): 
        for j in range(img_output.size[1]): 
            if direction=="C": 
                r, g, b = img_input.getpixel((j,img_output.size[0]-i-1)) 
            else: 
                r, g, b = img_input.getpixel((img_input.size[1]-j-1,i)) 
            pixels[i,j] = (r, g, b)
    
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB") 
    
    return img_output

# image rotate 180
def ImgRotatee(img_input,coldepth,direction): 

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if direction == "C180":
                r, g, b = img_input.getpixel((img_output.size[1]-i-1,img_output.size[0]-j-1))
            else:
                r, g, b = img_input.getpixel((img_output.size[0]-j-1, i))
            pixels[i,j] = (r, g, b)

    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB") 
    return img_output

# image rotate 270
def ImgRotate270(img_input,coldepth,direction):
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 
    
    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
    pixels = img_output.load() 
    for i in range(img_output.size[0]): 
        for j in range(img_output.size[1]): 
            if direction=="C270": 
                r, g, b = img_input.getpixel((img_input.size[1]-j-1,i)) 
            else: 
                r, g, b = img_input.getpixel((j,img_output.size[0]-i-1)) 
            pixels[i,j] = (r, g, b)
    
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB") 
    
    return img_output


def clipping(intensity):
    if intensity < 0:
        return 0
    if intensity > 255:
        return 255
    return intensity

def ChangeBrigness(imgInput, colDepth, changeValue): 
    #solusi 2 
    if colDepth!=24: 
        imgInput = imgInput.convert('RGB') 
    imgOutput = Image.new('RGB',(imgInput.size[1],imgInput.size[0])) 
    pixels = imgOutput.load() 

    for i in range(imgOutput.size[0]):
        for j in range(imgOutput.size[1]):
            r, g, b = imgInput.getpixel((i, j)) 
            pixels[i,j] = (clipping(r + changeValue), clipping(g+changeValue), clipping(b+changeValue)) 
    if colDepth==1: 
        imgOutput = imgOutput.convert("1") 
    elif colDepth==8: 
        imgOutput = imgOutput.convert("L") 
    else: 
        imgOutput = imgOutput.convert("RGB") 
 
    return imgOutput


def LogaritmicTransform(imgInput, colDepth, c):
    if colDepth!=24: 
        imgInput = imgInput.convert('RGB') 
    imgOutput = Image.new('RGB',(imgInput.size[1],imgInput.size[0])) 
    pixels = imgOutput.load() 

    for i in range(imgOutput.size[0]):
        for j in range(imgOutput.size[1]):
            r, g, b = imgInput.getpixel((i, j)) 
            pixels[i,j] = (int(c*math.log(1+r)), int(c*math.log(1+g)), int(c*math.log(1+b)))

    if colDepth==1: 
        imgOutput = imgOutput.convert("1") 
    elif colDepth==8: 
        imgOutput = imgOutput.convert("L") 
    else: 
        imgOutput = imgOutput.convert("RGB") 
 
    return imgOutput


def PowerLawTransform(imgInput, colDepth, gamma):
    if colDepth!=24: 
        imgInput = imgInput.convert('RGB') 
    imgOutput = Image.new('RGB',(imgInput.size[1],imgInput.size[0])) 
    pixels = imgOutput.load() 

    for i in range(imgOutput.size[0]):
        for j in range(imgOutput.size[1]):
            r, g, b = imgInput.getpixel((i, j)) 
            pixels[i,j] = (int(255*(r/255)**gamma), int(255*(r/255)**gamma), int(255*(b/255)**gamma))
    if colDepth==1: 
        imgOutput = imgOutput.convert("1") 
    elif colDepth==8: 
        imgOutput = imgOutput.convert("L") 
    else: 
        imgOutput = imgOutput.convert("RGB") 
 
    return imgOutput



# funtion for flipping images
def flipImage(imgInput, colDepth, direction):
    if colDepth!=24: 
        imgInput = imgInput.convert('RGB') 
    imgOutput = Image.new('RGB',(imgInput.size[1],imgInput.size[0])) 
    pixels = imgOutput.load() 

    for i in range(imgOutput.size[0]):
        for j in range(imgOutput.size[1]):
            r, g, b = imgInput.getpixel((i, j)) 
            if direction == "V":
                pixels[i,j] = (r, g, b)
            else:
                pixels[i,j] = (r, g, b)
    if colDepth==1: 
        imgOutput = imgOutput.convert("1") 
    elif colDepth==8: 
        imgOutput = imgOutput.convert("L") 
    else: 
        imgOutput = imgOutput.convert("RGB") 
 
    return imgOutput



def ImgTranslasi(img_input,coldepth,c,sumbu):
    
    if coldepth!=25: 
        img_input = img_input.convert('RGB') 
        img_input_pixels = img_input.load()

    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
    pixels = img_output.load() 

    for i in range(img_output.size[0]): 
        for j in range(img_output.size[1]): 
            r, g, b = img_input.getpixel((i, j))
            if sumbu == "x":
                if j+c < img_output.size[0]:
                    pixels[i,j] = img_input_pixels[i,j+c]
                else:
                    pixels[i,j] = (0, 0, 0)
            elif sumbu == "y":
                if i+c < img_output.size[0]:
                    pixels[i,j] = img_input_pixels[i+c,j]
                else:
                    pixels[i,j] = (0, 0, 0)
                
            
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB")
        
    return img_output

# translation x and y 
def ImgTranslasiXY(img_input,coldepth,cx,cy):
        
        if coldepth!=25: 
            img_input = img_input.convert('RGB') 
            img_input_pixels = img_input.load()
    
        img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
        pixels = img_output.load() 
    
        for i in range(img_output.size[0]): 
            for j in range(img_output.size[1]): 
                r, g, b = img_input.getpixel((i, j))
                if i+cx < img_output.size[0] and j+cy < img_output.size[1]:
                    pixels[i,j] = img_input_pixels[i+cx,j+cy]
                else:
                    pixels[i,j] = (0, 0, 0)
                    
                
        if coldepth==1: 
            img_output = img_output.convert("1") 
        elif coldepth==8: 
            img_output = img_output.convert("L") 
        else: 
            img_output = img_output.convert("RGB")
            
        return img_output


# funtion for flipping images
def ImgFlippingVertikal(img_input,coldepth):
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
            newPixels[i, verticalSize - j - 1] = (r, g, b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# function for flip image horizontal
def ImgFlippingHorizontal(img_input,coldepth):
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
            newPixels[horizontalSize - i - 1, j] = (r, g, b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# function for flip image horizontal and vertical
def ImgFlippingHorizontalVertical(img_input,coldepth):
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
            newPixels[horizontalSize - i - 1, verticalSize - j - 1] = (r, g, b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

 # image zoom in 
def ImgZoomIn(img_input,coldepth, n):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
 
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize*n, verticalSize*n))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            for k in range(n):
                for l in range(n):
                    newPixels[i*n+k, j*n+l] = (r, g, b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# images zoom out
def ImgZoomOut(img_input,coldepth, n):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
 
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize//n, verticalSize//n))
    newPixels = img_output.load()
    for i in range(horizontalSize//n):
        for j in range(verticalSize//n):
            r, g, b = pixels[i*n, j*n]
            newPixels[i, j] = (r, g, b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output



# TUGAS FUNGSI Gabungan
# funtion for grayscale image
def ImgGrayscale(img_input,coldepth):
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
            gray = (r + g + b) // 3
            newPixels[i, j] = (gray, gray, gray)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# funtion for half images is grayscale
def ImgHalfGrayscale(img_input,coldepth):
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
            if i < horizontalSize//2:
                gray = (r + g + b) // 3
                newPixels[i, j] = (gray, gray, gray)
            else:
                newPixels[i, j] = (r, g, b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


# funtion for diagonal images is grayscale
def ImgDiagonalGrayscale(img_input,coldepth):
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
            if i+j <= horizontalSize:
                if i < j:
                    
                    newPixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    newPixels[i, j] = (r, g, b)
            
            elif i+j > horizontalSize:
                if i > j:
                    newPixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    newPixels[i, j] = (r, g, b)
            
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# ini adalah fungsi saat latihan menuju UTS
# funtion for half images is grayscale and half images is negative
def ImgHalfGrayscaleNegative(img_input,coldepth):
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
            if i < horizontalSize//2:
                gray = (r + g + b) // 3
                newPixels[i, j] = (gray, gray, gray)
            else:
                newPixels[i, j] = (255-r, 255-g, 255-b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# 4 citra dengan semua fungsi flip dalam satu gambar 
def ImgFlip(img_input,coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
 
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize*2, verticalSize*2))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            newPixels[i, j] = (r, g, b)
            newPixels[i, verticalSize*2-1-j] = (r, g, b)
            newPixels[horizontalSize*2-1-i, j] = (r, g, b)
            newPixels[horizontalSize*2-1-i, verticalSize*2-1-j] = (r, g, b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# funtion for make circle in image and in circle is grayscale
def ImgCircleGrayscale(img_input,coldepth):
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
                if i < horizontalSize//2 and j < verticalSize//2:
                    gray = (r + g + b) // 3
                    newPixels[i, j] = (gray, gray, gray)
                elif i > horizontalSize//2 and j > verticalSize//2:
                    gray = (r + g + b) // 3
                    newPixels[i, j] = (gray, gray, gray)
                else :
                    newPixels[i, j] = (255-r,255-g, 255-b)
            else:
                newPixels[i, j] = (r, g, b)
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

# funtion for make diamond in image and in diamond is grayscale
def ImgDiamondGrayscale(img_input,coldepth):
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
            if abs(i-horizontalSize//2)+abs(j-verticalSize//2) < horizontalSize//2:
                gray = (r + g + b) // 3
                newPixels[i, j] = (gray, gray, gray)
            else:
                newPixels[i, j] = (r, g, b)
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output


# blend image with different size of image with images 2 is zoom out 2 time
def ImgBlend(img_input,img_input2,coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')
 
    pixels = img_input.load()
    pixels2 = img_input2.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    horizontalSize2 = img_input2.size[0]
    verticalSize2 = img_input2.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            r2, g2, b2 = pixels2[i*horizontalSize2//horizontalSize, j*verticalSize2//verticalSize]
            newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

# fungsi untuk zoomout
def ImgZoomOut2(img_input,coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
 
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize//2, verticalSize//2))
    newPixels = img_output.load()
    for i in range(horizontalSize//2):
        for j in range(verticalSize//2):
            r, g, b = pixels[i*2, j*2]
            newPixels[i, j] = (r, g, b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# fungsi untuk blend 2 gambar dengan ukuran yang berbeda
def BlendAPart(img_input, img_input2, coldepth): 
    if coldepth!=24:
        img_input2 = ImgZoomOut(img_input2, coldepth, 2)
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')
    
    
    pixels = img_input.load()
    pixels2 = img_input2.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    horizontalSize2 = img_input2.size[0]
    verticalSize2 = img_input2.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            if i < horizontalSize2 and j < verticalSize2:
                r, g, b = pixels[i, j]
                r2, g2, b2 = pixels2[i, j]
                newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            
            else:
                newPixels[i, j] = pixels[i, j]
            

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

# funtion for making 4 images in one output image
# 1 image is original image
# 2 image is flip vertical
# 3 image is flip horizontal
# 4 image is rotate 90 degree
def Img4in1(img_input,coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
 
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize*2, verticalSize*2))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            newPixels[i, j] = (r, g, b)
            newPixels[horizontalSize*2-i-1, j] = (r, g, b)
            newPixels[i, verticalSize*2-j-1] = (r, g, b)
            newPixels[horizontalSize*2-j-1,verticalSize*2-i-1 ] = (r, g, b)  
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

# funtion rotate 90 degree clockwise
def ImgRotate90(img_input,coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
 
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (verticalSize, horizontalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            newPixels[verticalSize-j-1, i] = (r, g, b)
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

# blend a part with zoom and rotate


def BlendAPartZoomRotate(img_input, img_input2, coldepth):
    if coldepth!=24:
        img_input2 = ImgZoomOut2(img_input2, coldepth)
        img_input2 = ImgRotate270(img_input2, coldepth)
        img_input = ImgFlippingHorizontal(img_input, coldepth)
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')
    
    
    pixels = img_input.load()
    pixels2 = img_input2.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    horizontalSize2 = img_input2.size[0]
    verticalSize2 = img_input2.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            # put the image 2 in the middle of image 1
            # if i > horizontalSize//2-horizontalSize2//2 and i < horizontalSize//2+horizontalSize2//2 and j > verticalSize//2-verticalSize2//2 and j < verticalSize//2+verticalSize2//2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2+horizontalSize2//2, j-verticalSize//2+verticalSize2//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the middle right of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2-verticalSize2//2 and j < verticalSize//2+verticalSize2//2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2+verticalSize2//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the button right of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the up right corner of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > 0 and j < verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the corner of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            if i< horizontalSize2 and j < verticalSize2:
                r, g, b = pixels[i, j]
                r2, g2, b2 = pixels2[i, j]
                newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            else:
                newPixels[i, j] = pixels[i, j]
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

    # return ImgFlippingVertikal(img_output, coldepth) 
# funtion for slice cross diagonal section of an image
def ImgSliceCrossDiagonal(img_input, coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            if i+j < horizontalSize:
                newPixels[i, j] = pixels[i, j]
            else:
                newPixels[i, j] = (0, 0, 0)
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output 

def ImgSliceCrossSection(img_input, coldepth):
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            newPixels[i, j] = (r, g, b)
            if i > horizontalSize//2-1 and i < horizontalSize//2+1:
                newPixels[i, j] = (0, 0, 0)
            if j > verticalSize//2-1 and j < verticalSize//2+1:
                newPixels[i, j] = (0, 0, 0)
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# function for rotate 270 degree
def ImgRotate270(img_input, coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (verticalSize, horizontalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            newPixels[j, horizontalSize-i-1] = (r, g, b)
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

# function for rotate 180 degree
def ImgRotate180(img_input, coldepth):
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
            newPixels[horizontalSize-i-1, verticalSize-j-1] = (r, g, b)
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


def BlendAPartZoomRotate2(img_input, img_input2, coldepth):
    if coldepth!=24:
        img_input2 = ImgZoomOut2(img_input2, coldepth)
        img_input2 = ImgRotate270(img_input2, coldepth)
        # img_input2 = ImgRotate90(img_input2, coldepth)
        img_input = ImgFlippingHorizontal(img_input, coldepth)
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')
    
    
    pixels = img_input.load()
    pixels2 = img_input2.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    horizontalSize2 = img_input2.size[0]
    verticalSize2 = img_input2.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            # put the image 2 in the middle of image 1
            # if i > horizontalSize//2-horizontalSize2//2 and i < horizontalSize//2+horizontalSize2//2 and j > verticalSize//2-verticalSize2//2 and j < verticalSize//2+verticalSize2//2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2+horizontalSize2//2, j-verticalSize//2+verticalSize2//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the middle right of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2-verticalSize2//2 and j < verticalSize//2+verticalSize2//2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2+verticalSize2//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the button right of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the up right corner of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > 0 and j < verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the corner of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            if i< horizontalSize2 and j < verticalSize2:
                r, g, b = pixels[i, j]
                r2, g2, b2 = pixels2[i, j]
                newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            else:
                newPixels[i, j] = pixels[i, j]
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

def BlendAPartZoomRotate3(img_input, img_input2, coldepth):
    if coldepth!=24:
        img_input2 = ImgZoomOut2(img_input2, coldepth)
        # img_input2 = ImgRotate270(img_input2, coldepth)
        # img_input2 = ImgRotate90(img_input2, coldepth)
        # img_input = ImgFlippingHorizontal(img_input, coldepth)
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')
    
    
    pixels = img_input.load()
    pixels2 = img_input2.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    horizontalSize2 = img_input2.size[0]
    verticalSize2 = img_input2.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            # put the image 2 in the middle of image 1
            # if i > horizontalSize//2-horizontalSize2//2 and i < horizontalSize//2+horizontalSize2//2 and j > verticalSize//2-verticalSize2//2 and j < verticalSize//2+verticalSize2//2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2+horizontalSize2//2, j-verticalSize//2+verticalSize2//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the middle right of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2-verticalSize2//2 and j < verticalSize//2+verticalSize2//2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2+verticalSize2//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the button right of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the up right corner of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > 0 and j < verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # put the image 2 in the corner of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]
            
          

            # put the image 2 in right corner up of image 1
            if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2-verticalSize2 and j < verticalSize//2:
                r, g, b = pixels[i, j]
                r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2+verticalSize2]
                newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            else:
                newPixels[i, j] = pixels[i, j]

            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > 0 and j < verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     newPixels[i, j] = pixels[i, j]

            # if i< horizontalSize2 and j < verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i, j]
            #     newPixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
                # newPixels[i, j] = pixels[i, j]
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return ImgRotate180(img_output, coldepth)


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


# fungsi untuk neighborhood operation 
# statistical filtering 
# median filter
# funtion pixel replication



def PixelReplication(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    # make a mask 5*5 for the image 
    
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            if i % 2 == 0 and j % 2 == 0:
                newPixels[i, j] = (r, g, b)
                newPixels[i+1, j] = (r, g, b)
                newPixels[i, j+1] = (r, g, b)
                newPixels[i+1, j+1] = (r, g, b)
            elif i % 2 == 0 and j % 2 != 0:
                newPixels[i, j] = (r, g, b)
                newPixels[i+1, j] = (r, g, b)
            elif i % 2 != 0 and j % 2 == 0:
                newPixels[i, j] = (r, g, b)
                newPixels[i, j+1] = (r, g, b)
            else:
                newPixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output 



def MedianFilter(img_input, coldepth):
    if coldepth!=24:
        img_input=PixelReplication(img_input, coldepth)
        img_input = img_input.convert('RGB')
    

    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(1,horizontalSize-1):
        for j in range(1,verticalSize-1):
    #         r = []
    #         g = []
    #         b = []
    #         for k in range(3):
    #             for l in range(3):
    #                 r.append(pixels[i+k-2,j+l-2][0])
    #                 g.append(pixels[i+k-2,j+l-2][1])
    #                 b.append(pixels[i+k-2,j+l-2][2])
    #         r.sort()
    #         g.sort()
    #         b.sort()
    #         newPixels[i,j] = (r[4],g[4],b[4])

            r1, g1, b1 = pixels[i-1, j-1]
            r2, g2, b2 = pixels[i-1, j]
            r3, g3, b3 = pixels[i-1, j+1]
            r4, g4, b4 = pixels[i, j-1]
            r5, g5, b5 = pixels[i, j]
            r6, g6, b6 = pixels[i, j+1]
            r7, g7, b7 = pixels[i+1, j-1]
            r8, g8, b8 = pixels[i+1, j]
            r9, g9, b9 = pixels[i+1, j+1]
            r = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
            g = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
            b = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
            r.sort()
            g.sort()
            b.sort()
            newPixels[i, j] = (r[4], g[4], b[4])
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output


# mean filter
def MeanFilter(img_input, coldepth):
    if coldepth!=24:
        img_input=PixelReplication(img_input, coldepth)
        img_input = img_input.convert('RGB')
 
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    for i in range(1,horizontalSize-1):
        for j in range(1,verticalSize-1):
            r1, g1, b1 = pixels[i-1, j-1]
            r2, g2, b2 = pixels[i-1, j]
            r3, g3, b3 = pixels[i-1, j+1]
            r4, g4, b4 = pixels[i, j-1]
            r5, g5, b5 = pixels[i, j]
            r6, g6, b6 = pixels[i, j+1]
            r7, g7, b7 = pixels[i+1, j-1]
            r8, g8, b8 = pixels[i+1, j]
            r9, g9, b9 = pixels[i+1, j+1]
            r = (r1+r2+r3+r4+r5+r6+r7+r8+r9)//9
            g = (g1+g2+g3+g4+g5+g6+g7+g8+g9)//9
            b = (b1+b2+b3+b4+b5+b6+b7+b8+b9)//9
            newPixels[i, j] = (r, g, b)
        
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

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


# mean filter with mask size adjustable
def MeanFilter2(img_input, coldepth, maskSize):
    if coldepth!=24:
        img_input=PixelReplication(img_input, coldepth)
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
        img_input=PixelReplication(img_input, coldepth)
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