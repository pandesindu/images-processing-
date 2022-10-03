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
        sg.Button("Image Rotate", size=(20, 1), key="ImgRotate"), 
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
            img_output=ImgRotate(img_input,coldepth,90,"C") 
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
            img_output=ImagesBlending(img_input,input_image2,coldepth) 
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
            # value = int(values["sliderBrigness"])
            window["ImgProcessingType"].update("Power Law") 
            img_output=PowerLawTransform(img_input,coldepth,10) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass



# window.close()

