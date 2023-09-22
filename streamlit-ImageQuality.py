import os
import numpy as np
import streamlit as st
from csv import writer
from xlwt import Workbook
from PIL import Image
import glob
#import cv2


#path_g="/home/shubhangi/StreamlitPRJ/Output/good/"
#path_b="/home/shubhangi/StreamlitPRJ/Output/bad/"
#path_u="/home/shubhangi/StreamlitPRJ/Output/uncertain/"
#path_face="/home/shubhangi/StreamlitPRJ/CutFaces"

path_g="./Output/good/"
path_b="./Output/bad/"
path_c="./Output/confused/"
path_face="./CutFaces"
path_processed = "./Processed_Images/"
Attributes = np.zeros((8))
  
if __name__ == '__main__':
    st.title("Azadi ka Amrutmahotsav DoT SPPU Image Quality Check")
    # list files in img directory
    #path=st.text_input("Mention the path of image folder")

    #path="./TestImages/"
    #path = glob.glob('./Images/*/*.jpg', recursive=True) # for Linux
    path = glob.glob('.\\Images\\*\\*.jpg', recursive=True) # for Windows
    basepath, basame = os.path.split(path[0])
    list_path = [os.path.basename(x) for x in path]

    

    #files = os.listdir(path)
    # print(files)
    image_name = st.sidebar.selectbox("Image Name", list_path)
    #img=Image.open(basepath+'/'+image_name) # for Linux
    img=Image.open(basepath+'\\'+image_name) # for Windows

    st.image(img)
    #print(path+image_name)
    ############################################################
    # drawing_mode = st.sidebar.selectbox(
    #    "Drawing tool:", ("rect","")
    # )
    # realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
    #realtime_update = 'True'
    #box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
    # aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
    #aspect_dict = {
    #  "1:1": (1, 1),
    #  "16:9": (16, 9),
    #  "4:3": (4, 3),
    #  "2:3": (2, 3),
    #  "Free": None
    #}
    #aspect_ratio = aspect_dict[aspect_choice]
    #aspect_ratio = (1, 1)
    if image_name:
       #img = Image.open(path+image_name)
       #if not realtime_update:
         # st.write("Double click to save crop")
       # Get a cropped image from the frontend
       #cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                              # aspect_ratio=aspect_ratio)
       # Manipulate cropped image at will
       # st.write("Preview")
       #_ = cropped_img.thumbnail((150,150))
       # st.image(cropped_img) 

    ###############################################
    # Workbook is created
     wb = Workbook()
     # add_sheet is used to create sheet.
     sheet1 = wb.add_sheet('Sheet 1')
     sheet1.write(0, 1, 'Quality')
     #####column #####
     sheet1.write(1, 0, image_name)
    ################################################
   
    ################ Attributes ################
    ################################################
    #st.markdown("")
     img_quality = st.sidebar.radio(
      "Image Quality",
      ('Good', 'Bad', 'Confused'))
       
   
     if st.sidebar.button('SAVE'):
      
        if img_quality == 'Good':
          sheet1.write(1, 1, img_quality)
          img.save(path_g+image_name)
          base_filename = os.path.basename(image_name)
          title, ext = os.path.splitext(base_filename) 
         #final_filepath = os.path.join(path_face,title)
         #cropped_img.save(path_face,"BMP" )
         #cropped_img.save('./CutFaces/{}.jpg'.format(title)) 
        if img_quality== 'Bad':
          sheet1.write(1, 1, img_quality)
          img.save(path_b+image_name)
        if img_quality== 'Confused':
          sheet1.write(1, 1, img_quality)
          img.save(path_c+image_name)

        Attributes=[image_name,img_quality]
      #print(Attributes)
       #np.savetxt("my_output_file.csv", Attributes, delimiter=",")

        with open('Report.csv', 'a',newline='') as nums:
           writer_obj = writer(nums)
           writer_obj.writerow(Attributes)
           nums.close()
        st.sidebar.write('Image Processed Succesfully') 

        img.save(path_processed+image_name)
        #rm = os.remove(basepath+'/'+image_name)
        rm = os.remove(basepath+'\\'+image_name)      
      
         

    
    
    
    
    
    
       
    
    
    
    
    
    
    
    
    




