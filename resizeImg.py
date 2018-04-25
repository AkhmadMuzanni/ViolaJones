# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:32:22 2018

@author: USER
"""

import PIL
from PIL import Image

#ubah berdasarkan width
def ubahWidth():
    basewidth = 100
    img = Image.open('bahan/download.jpg')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save('resized_image.jpg')

#ubah berdasarkan height
def ubahHeight():
    baseheight = 40
    img = Image.open('bahan/1.jpg')
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    imgUbah = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    imgUbah.save('ubah.jpg')

ubahHeight();