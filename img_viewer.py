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
        sg.Text("Rotation"), 
    ], 
    [ 
        sg.Button("Rotate 90", size=(10, 1), key="ImgRotate"),
        sg.Button("Rotate 180", size=(10, 1), key="ImgRotate180"),
        sg.Button("Rotate 270", size=(10, 1), key="ImgRotate270"), 
    ], 
    [ 
        sg.Text("Change Brightness"), 
    ], 
    [
        sg.Slider(range=(-255,255), orientation="h", size=(19,20), key="sliderBrigness", default_value=0),
        sg.Button("Change Brigness", size=(15, 1), key="ImgChangeBrigness"),
        
    ],
    [ 
        sg.Text("Blending"), 
    ],  
    [
        sg.In(size=(15, 1), enable_events=True, key="inputImage2"),
        sg.FileBrowse(),
        sg.Button("Blending Images", size=(20, 1), key="ImgBlending")
    ],
    [ 
        sg.Text("Tranformation"), 
    ],  
    [
        sg.Button("Logaritmic Transform", size=(15, 1), key="ImgLogaritmicTransform"),
        sg.Button("Power Law", size=(10, 1), key="ImgPowerLaw")
    ],
    [ 
        sg.Text("Translation"), 
    ], 
    [
        # input value translation 
        sg.Text("Value"),
        sg.In(size=(20,10), key = "inputNilaiTranslasi"), 
    ],
    [
        sg.Button("Translasi X", size=(12, 1), key="ImgTranslationX"),
        sg.Button("Translasi Y", size=(12, 1), key="ImgTranslationY"),
        sg.Button("Translasi XY", size=(12, 1), key="ImgTranslationXY")
    ],
    [ 
        sg.Text("Fliiping"), 
    ], 
    [
        # button for flipping vertical 
        sg.Button("Flip Vertical", size=(12, 1), key="ImgFlipVertical"),
        sg.Button("Flip Horizontal", size=(12, 1), key="ImgFlipHorizontal"),
        sg.Button("Flip Vertical and Horizontal", size=(20, 1), key="ImgVertikalHorozontal"),
    ], 
    [ 
        sg.Text("Zooming"), 
    ], 

    [
        # slider for zoom in 
        sg.Slider(range=(1,10), orientation="h", size=(19,20), key="sliderZoom", default_value=1),
        # button for zoom in
        sg.Button("Zoom In", size=(10, 1), key="ImgZoomIn"),
        sg.Button("Zoom Out", size=(10, 1), key="ImgZoomOut"),
    ],
 
    # [
    #     # button for grayscaling 
    #     sg.Button("Grayscaling", size=(20, 1), key="ImgGrayscaling"),
    # ], 
    # [
    #     # text UTS and underline 
    #     sg.Text("UTS", font=("Helvetica", 12), text_color="black"),
    # ], 
    # [
    #     # button for shape in image 
    #     # button shape circle 
    #     sg.Button("Shape Circle", size=(20, 1), key="ImgShapeCircle"),
    #     # button shape diamond
    #     sg.Button("Shape Diamond", size=(20, 1), key="ImgShapeDiamond"),
    #     # button shape cross
    #     sg.Button("Shape Cross", size=(20, 1), key="ImgShapeCross"),
    # ], 
    # [
    #     # button 4 image flip 
    #     sg.Button("Flip 4 Image", size=(20, 1), key="ImgFlip4Image"),
    #     # button 4 image flip and rotate
    #     sg.Button("Flip and Rotate 4 Image", size=(20, 1), key="ImgFlipRotate4Image"),
    # ], 
    # [
    #     # button blend 
    #     sg.Button("Blend dif size", size=(20, 1), key="ImgBlendImage"),
    #     # button blend and rotate
    #     sg.Button("Blend and Rotate dif size", size=(20, 1), key="ImgBlendRotateImage"),
    #     # button blend and rotate and flip
    #     sg.Button("Blend and Flip dif size", size=(20, 1), key="ImgBlendRotateFlipImage"),
    # ], 
    # [
    #     sg.Button("UTS Wajib", size=(20, 1), key="UtsWajib"),
    #     sg.Button("UTS Bonus", size=(20, 1), key="UtsBonus"),
    # ]


    # neigborhood processing
    [
        sg.Text("Neighborhood Processing"),
    ],
    [
        # button median filter
        sg.Button("Median Filter", size=(20, 1), key="ImgMedianFilter"),
        # mean filter
        sg.Button("Mean Filter", size=(20, 1), key="ImgMeanFilter"),

    ], 
    [
        # button max filter
        sg.Button("Max Filter", size=(20, 1), key="ImgMaxFilter"),
        # button min filter
        sg.Button("Min Filter", size=(20, 1), key="ImgMinFilter"),
    ], 
    [
        # WeightedAverageFilter
        sg.Button("Weighted Average Filter", size=(20, 1), key="ImgWeightedAverageFilter"),
    ],
    [
        # low pass filter
        sg.Text("Low and High Pass Filter"),
    ], 
    [
        #first gradient filter
        sg.Button("First Gradient Filter", size=(20, 1), key="ImgFirstGradientFilter"),
        # center gradient filter
        sg.Button("Center Diferentces Filter", size=(20, 1), key="ImgCenterGradientFilter"),
    ], 
    [
        # roberts filter
        sg.Button("Roberts Filter", size=(20, 1), key="ImgRobertsFilter"),
        # prewitt filter
        sg.Button("Prewitt Filter", size=(20, 1), key="ImgPrewittFilter"),

    ], 
    [
        # sobel filter
        sg.Button("Sobel Filter", size=(20, 1), key="ImgSobelFilter"),
        # laplacian filter
        sg.Button("Laplacian Filter", size=(20, 1), key="ImgLaplacianFilter"),
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
    
    # pointwise operation
    # image negative
    elif event == "ImgNegative": 

        try: 
            window["ImgProcessingType"].update("Image Negative") 
            img_output=ImgNegative(img_input,coldepth) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
    
    # image rotation
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
    

    elif event == "ImgRotate270":
        try: 
            window["ImgProcessingType"].update("Image Rotate") 
            img_output=ImgRotate(img_input,coldepth,"C270") 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass

    # brigeness chage
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
            img_output=ImgBlend(img_input,input_image2,coldepth) 
            # print(img_output)
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out)

        except: 
            pass
    

    # tranformation
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
    
    elif event == "ImgTranslationXY" :
        try:
            value1 = int(values["inputNilaiTranslasi"])
            value2 = int(values["inputNilaiTranslasi"])
            window["ImgProcessingType"].update("Translation")
            img_output=ImgTranslasiXY(img_input,coldepth,value1,value2)
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
            value = int(values["sliderZoom"])
            window["ImgProcessingType"].update("Zoom In")
            img_output=ImgZoomIn(img_input,coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgZoomOut":
        try:
            value = int(values["sliderZoom"])
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

    elif event == "UtsWajib":
        try:
            window["ImgProcessingType"].update("Grayscale")
            img_output=ImgCircleAndDiamond(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass  

    elif event == "UtsBonus":
        try:
            window["ImgProcessingType"].update("Grayscale")
            img_output=BonusUts(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgMedianFilter":
        try:
            window["ImgProcessingType"].update("median filter")
            img_output=MedianFilter2(img_input,coldepth,5)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgMeanFilter":
        try:
            
            window["ImgProcessingType"].update("mean filter")
            img_output=MeanFilter2(img_input,coldepth,3)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgMinFilter":
        try:
            window["ImgProcessingType"].update("min filter")
            img_output=MinFilter(img_input,coldepth,3)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgMaxFilter":
        try:
            window["ImgProcessingType"].update("max filter")
            img_output=MaxFilter(img_input,coldepth,3)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgWeightedAverageFilter":
        try:
            window["ImgProcessingType"].update("weighted average filter")
            img_output=WeightedAverageFilter(img_input,coldepth,3)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFirstGradientFilter":
        try:
            window["ImgProcessingType"].update("first gradient filter")
            img_output=FirstGradientFilter(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgCenterGradientFilter":
        try:
            window["ImgProcessingType"].update("center diferences filter")
            img_output=CenterDifferenceFilter(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    # robert filter
    elif event == "ImgRobertsFilter":
        try:
            window["ImgProcessingType"].update("robert filter")
            img_output=RobertsFilter(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    # sobel filter
    elif event == "ImgSobelFilter":
        try:
            window["ImgProcessingType"].update("sobel filter")
            img_output=SobelFilter(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    # prewitt filter
    elif event == "ImgPrewittFilter":
        try:
            window["ImgProcessingType"].update("prewitt filter")
            img_output=PrewittFilter(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    # laplacian filter
    elif event == "ImgLaplacianFilter":
        try:
            window["ImgProcessingType"].update("laplacian filter")
            img_output=LaplacianFilter(img_input,coldepth,3)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
