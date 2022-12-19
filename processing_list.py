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
