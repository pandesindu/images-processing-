import PySimpleGUI as sg 
import os.path 
from PIL import Image, ImageOps
from  processing_list import *
# Kolom Area No 1: Area open folder and select image 
file_list_column = [ 
    [ 
        sg.Text("Open Image Folder :"), 
    ], 
    [ 
        sg.In(size=(20, 1), enable_events=True, key="ImgFolder"), 
        sg.FolderBrowse(), 
    ], 
    [ 
        sg.Text("Choose an image from list :"), 
    ], 
    [ 
        sg.Listbox( 
        values=[], enable_events=True, size=(18, 10), key="ImgList" 
        ) 
    ], 
]

# Kolom Area No 2: Area viewer image input 
image_viewer_column = [ 
    [sg.Text("Image Input :")], 
    [sg.Text(size=(40, 1), key="FilepathImgInput")], 
    [sg.Image(key="ImgInputViewer")], 
]


# Kolom Area No 3: Area Image info dan Tombol list of processing 
list_processing = [ 
    [ 
        sg.Text("Image Information:"), 
    ], 
    [ 
        sg.Text(size=(20, 1), key="ImgSize"), 
    ], 
    [ 
        sg.Text(size=(20, 1), key="ImgColorDepth"), 
    ], 
    [ 
        sg.Text("List of Processing:"), 
    ], 
    [ 
        sg.Button("Image Negative", size=(20, 1), key="ImgNegative"), 
    ], 
    [ 
        sg.Button("Image Rotate 90", size=(20, 1), key="ImgRotate"),
        sg.Button("Image Rotate 180", size=(20, 1), key="ImgRotate180"), 
    ], 
    [
        sg.Slider(range=(-255,255), orientation="h", size=(19,20), key="sliderBrigness", default_value=0),
        sg.Button("Change Brigness", size=(20, 1), key="ImgChangeBrigness"),
        
    ], 
    [
        sg.In(size=(15, 1), enable_events=True, key="inputImage2"),
        sg.FileBrowse(),
        sg.Button("Blending Images", size=(20, 1), key="ImgBlending")
    ], 
    [
        sg.Button("Logaritmic Transform", size=(20, 1), key="ImgLogaritmicTransform")
    ],
    [
        sg.Button("Power Law", size=(20, 1), key="ImgPowerLaw")
    ],
    [
        # input value translation 
        sg.Text("nilai translasi"),
        sg.In(size=(20,10), key = "inputNilaiTranslasi"),
        # button for translation
        sg.Button("Translasi X", size=(20, 1), key="ImgTranslationX"),
        sg.Button("Translasi Y", size=(20, 1), key="ImgTranslationY")
    ],
    [
        # button for flipping vertical 
        sg.Button("Flip Vertical", size=(20, 1), key="ImgFlipVertical"),
        sg.Button("Flip Horizontal", size=(20, 1), key="ImgFlipHorizontal"),
    ], 
    [
        # button for flipping vertical and horizontal
        sg.Button("Flip Vertical and Horizontal", size=(20, 1), key="ImgVertikalHorozontal"),
    ],
    [
        # slider for zoom in 
        sg.Slider(range=(1,10), orientation="h", size=(19,20), key="sliderZoomIn", default_value=1),
        # button for zoom in
        sg.Button("Zoom In", size=(20, 1), key="ImgZoomIn"),
    ],
    [
        # slider for zoom out
        sg.Slider(range=(1,10), orientation="h", size=(19,20), key="sliderZoomOut", default_value=1),
        # button for zoom out
        sg.Button("Zoom Out", size=(20, 1), key="ImgZoomOut"),
    ], 
    [
        # button for grayscaling 
        sg.Button("Grayscaling", size=(20, 1), key="ImgGrayscaling"),
    ], 
    [
        # text UTS and underline 
        sg.Text("UTS", font=("Helvetica", 12), text_color="black"),
    ], 
    [
        # button for shape in image 
        # button shape circle 
        sg.Button("Shape Circle", size=(20, 1), key="ImgShapeCircle"),
        # button shape diamond
        sg.Button("Shape Diamond", size=(20, 1), key="ImgShapeDiamond"),
        # button shape cross
        sg.Button("Shape Cross", size=(20, 1), key="ImgShapeCross"),
    ], 
    [
        # button 4 image flip 
        sg.Button("Flip 4 Image", size=(20, 1), key="ImgFlip4Image"),
        # button 4 image flip and rotate
        sg.Button("Flip and Rotate 4 Image", size=(20, 1), key="ImgFlipRotate4Image"),
    ], 
    [
        # button blend 
        sg.Button("Blend dif size", size=(20, 1), key="ImgBlendImage"),
        # button blend and rotate
        sg.Button("Blend and Rotate dif size", size=(20, 1), key="ImgBlendRotateImage"),
        # button blend and rotate and flip
        sg.Button("Blend and Flip dif size", size=(20, 1), key="ImgBlendRotateFlipImage"),
    ]

    
] 


# Kolom Area No 4: Area viewer image output 
image_viewer_column2 = [ 
    [sg.Text("Image Processing Output:")], 
    [sg.Text(size=(40, 1), key="ImgProcessingType")], 
    [sg.Image(key="ImgOutputViewer")], 
] 


# Gabung Full layout 
layout = [ 
    [ 
    sg.Column(file_list_column), 
    sg.VSeperator(), 
    sg.Column(image_viewer_column), 
    sg.VSeperator(), 
    sg.Column(list_processing), 
    sg.VSeperator(), 
    sg.Column(image_viewer_column2), 
    ] 
] 

window = sg.Window("Mini Image Editor", layout) 

#nama image file temporary setiap kali processing output 
filename_out = "out.png" 
# Run the Event Loop 
while True:
    event, values = window.read() 
    if event == "Exit" or event == sg.WIN_CLOSED: 
        break 
    
    # Folder name was filled in, make a list of files in the folder 
    if event == "ImgFolder": 
        folder = values["ImgFolder"] 
        try: 
        # Get list of files in folder 
            file_list = os.listdir(folder) 
        except: 
            file_list = [] 
        fnames = [ 
            f 
            for f in file_list 
            if os.path.isfile(os.path.join(folder, f)) 
            and f.lower().endswith((".png", ".gif")) 
        ] 
        window["ImgList"].update(fnames)
    elif event == "ImgList": # A file was chosen from the listbox 
        try: 
            filename = os.path.join( 
            values["ImgFolder"], values["ImgList"][0] 
            ) 
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename) 
            window["ImgProcessingType"].update(filename) 
            window["ImgOutputViewer"].update(filename=filename) 
            img_input = Image.open(filename) 
            #img_input.show() 
            
            #Size 
            img_width, img_height = img_input.size 
            window["ImgSize"].update("Image Size : "+str(img_width)+" x "+str(img_height)) 
            
            #Color depth 
            mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 
            24, "HSV": 24, "I": 32, "F": 32} 
            coldepth = mode_to_coldepth[img_input.mode] 
            window["ImgColorDepth"].update("Color Depth : "+str(coldepth)) 
        except: 
            pass
    elif event == "ImgNegative": 

        try: 
            window["ImgProcessingType"].update("Image Negative") 
            img_output=ImgNegative(img_input,coldepth) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
    elif event == "ImgRotate": 

        try: 
            window["ImgProcessingType"].update("Image Rotate") 
            img_output=ImgRotate(img_input,coldepth,"C") 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass

    elif event == "ImgRotate180": 

        try: 
            window["ImgProcessingType"].update("Image Rotate") 
            img_output=ImgRotatee(img_input,coldepth,"C180") 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass


    
    elif event == "ImgChangeBrigness": 

        try: 
            value = int(values["sliderBrigness"])
            window["ImgProcessingType"].update("brigness") 
            img_output=ChangeBrigness(img_input,coldepth,value) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass

    elif event == "ImgBlending": 
 
        try: 
            filename = values['inputImage2']
            input_image2 = Image.open(filename)
            # print(filename)
            window["ImgProcessingType"].update("Blending Images") 
            img_output=BlendAPartZoomRotate3(img_input,input_image2,coldepth) 
            # print(img_output)
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out)

        except: 
            pass
    
    elif event == "ImgLogaritmicTransform": 

        try: 
            # value = int(values["sliderBrigness"])
            window["ImgProcessingType"].update("Logaritmic Transform") 
            img_output=LogaritmicTransform(img_input,coldepth,50) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass

    elif event == "ImgPowerLaw": 

        try: 
            
            window["ImgProcessingType"].update("Power Law") 
            img_output=PowerLawTransform(img_input,coldepth,10) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass

    elif event == "ImgTranslationX" :
        try:
            value = int(values["inputNilaiTranslasi"])
            window["ImgProcessingType"].update("Translation")
            img_output=ImgTranslasi(img_input,coldepth,value,"x")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgTranslationY" :
        try:
            value = int(values["inputNilaiTranslasi"])
            window["ImgProcessingType"].update("Translation")
            img_output=ImgTranslasi(img_input,coldepth,value,"y")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlipVertical":
        try:
            window["ImgProcessingType"].update("Translation Image")
            img_output=ImgFlippingVertikal(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlipHorizontal":
        try:
            window["ImgProcessingType"].update("Translation Image")
            img_output=ImgFlippingHorizontal(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgVertikalHorozontal":
        try:
            window["ImgProcessingType"].update("Translation Image")
            img_output=ImgFlippingHorizontalVertical(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgZoomIn":
        try:
            value = int(values["sliderZoomIn"])
            window["ImgProcessingType"].update("Zoom In")
            img_output=ImgZoomIn(img_input,coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgZoomOut":
        try:
            value = int(values["sliderZoomOut"])
            window["ImgProcessingType"].update("Zoom Out")
            img_output=ImgZoomOut(img_input,coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    # grayscaling 
    elif event == "ImgGrayscaling":
        try:
            window["ImgProcessingType"].update("Grayscale")
            img_output=ImgCircleGrayscale(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgShapeCircle":
        try:
            window["ImgProcessingType"].update("Grayscale")
            img_output=ImgCircleGrayscale(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgShapeDiamond": 
        try: 
            window["ImgProcessingType"].update("Grayscale") 
            img_output=ImgDiamondGrayscale(img_input,coldepth) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass

    elif event == "ImgShapeCross":
        try:
            window["ImgProcessingType"].update("Grayscale")
            img_output=ImgDiagonalGrayscale(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass 

    elif event == "ImgFlip4Image":
        try:
            window["ImgProcessingType"].update("Grayscale")
            img_output=ImgFlip(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass         

    elif event == "ImgFlipRotate4Image":
        try:
            window["ImgProcessingType"].update("Grayscale")
            img_output=Img4in1(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass  

    elif event == "ImgBlendImage": 
 
        try: 
            filename = values['inputImage2']
            input_image2 = Image.open(filename)
            window["ImgProcessingType"].update("Blending Images") 
            img_output=BlendAPart(img_input,input_image2,coldepth) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out)

        except: 
            pass

    elif event == "ImgBlendRotateImage":
        try: 
            filename = values['inputImage2']
            input_image2 = Image.open(filename)
            window["ImgProcessingType"].update("Blending Images") 
            img_output=BlendAPartZoomRotate(img_input,input_image2,coldepth) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out)

        except: 
            pass

    elif event == "ImgBlendRotateFlipImage":
        try: 
            filename = values['inputImage2']
            input_image2 = Image.open(filename)
            window["ImgProcessingType"].update("Blending Images") 
            img_output=BlendAPartZoomRotate3(img_input,input_image2,coldepth) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out)

        except: 
            pass