import math
from PIL import Image, ImageOps 
def ImgNegative(img_input,coldepth): 
    #solusi 1 
    #img_output=ImageOps.invert(img_input) 
    #solusi 2 
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

def ImgRotate(img_input,coldepth,deg,direction): 
    #solusi 1 
    #img_output=img_input.rotate(deg) 
    
    #solusi 2 
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


def ImagesBlending(imgInput1, imgInput2, colDepth):
    # print(imgInput1, imgInput2)
    if colDepth!=24: 
        imgInput1 = imgInput1.convert('RGB')
        imgInput2 = imgInput2.convert('RGB')
        # print(imgInput1, imgInput2)
        
    imgOutput = Image.new('RGB',(imgInput1.size[1], imgInput1.size[0])) 
    pixels = imgOutput.load() 
    for i in range(imgOutput.size[0]):
        for j in range(imgOutput.size[1]):
            r, g, b = imgInput1.getpixel((i, j))
            r1, g1, b1 = imgInput2.getpixel((i, j))
            blendR, blendG, blendB = r+r1, g+g1, b+b1
            pixels[i,j] = (blendR, blendG, blendB )

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



        



        