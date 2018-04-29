# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:32:22 2018

@author: USER
"""

import PIL
from PIL import Image

#ubah berdasarkan width
def ubahWidth():
    basewidth = 20
    img = Image.open('bahan/1.jpg')
    #wpercent = (basewidth / float(img.size[0]))
    #hsize = int((float(img.size[1]) * float(wpercent)))
    hsize = 40
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    txtHeight = str(hsize)
    txtWidth = str(basewidth)
    img.save('resized_image'+txtHeight+'x'+txtWidth+'.jpg')

#ubah berdasarkan height
def ubahHeight():
    baseheight = 40
    img = Image.open('bahan/1.jpg')
    #hpercent = (baseheight / float(img.size[1]))
    #wsize = int((float(img.size[0]) * float(hpercent)))
    wsize = 20
    imgUbah = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    txtHeight = str(baseheight)
    txtWidth = str(wsize)
    imgUbah.save('resized_image'+txtHeight+'x'+txtWidth+'.jpg')

ubahHeight();