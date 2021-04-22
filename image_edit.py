import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path


dir_name = "image"#入手先フォルダ
new_dir_name = "edit_lavender_whole"#保存先フォルダ

#整合性を取る必要あり
(img_width_ratio,img_height_ratio) = (1,1)#画像の比率
(size_width,size_height) = (416,416)#画像のサイズ

i=1


#実装
imagefiles = os.listdir(dir_name)
for filename in imagefiles:
  filepath = os.path.join(dir_name, filename)
  if os.path.isfile(filepath) :
        
    img = Image.open(filepath)

    
    #トリミング    
    center_x = int(img.width / 2)#中心のx座標
    center_y = int(img.height / 2)#中心のy座標
    
    size = img.height/img_width_ratio
    img_size_width = size*img_width_ratio#画像の横幅
    img_size_height = size*img_height_ratio#画像の縦幅
    
    img = img.crop((center_x - img_size_width / 2, center_y - img_size_height / 2, center_x +img_size_width / 2, center_y + img_size_height / 2))

    #リサイズ
    #img = img.resize((size_width,size_height))
    
    
    img.save(os.path.join(new_dir_name,("lavender" + (str(i).zfill(3)) +".jpg")))
    i += 1
print(i-1)