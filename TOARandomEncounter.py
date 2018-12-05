
# coding: utf-8

# In[ ]:


from matplotlib.pyplot import imshow, show
import numpy as np
from PIL import Image
import pytesseract
get_ipython().run_line_magic('matplotlib', 'inline')

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


# In[ ]:


def get_average_color(x, n, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""
    x, y = x
    r, g, b = 0, 0, 0
    count = 0
    
    for s in range(x, image.width):
        for t in range(y, image.height):
            rgb_im = image.convert('RGB')
          
            pixlr,  pixlg, pixlb= rgb_im.getpixel((s, t))
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    return ((r/count), (g/count), (b/count))


img = Image.open('toaMap.jpg')
numbers = Image.open('just numbers.png')
width = 67
for x in range (2, int(img.width/width)):
    for y in range (2, int(img.height/width)):
        if x%2 == 0: y = y-.5
        if y%2 == 0: x = x-.5
        
        crop_rectangle = ((x*width)+30,30 + y*width,((x+1)*width)+30  ,30 + (y+1)*width )
        
        cropped_im = img.crop(crop_rectangle)
        numbers_cropped = numbers.crop(crop_rectangle)
        
        number ={}

        if x%1 ==0:
            print("rectangle: {}, image average: {}".format( (y*int(img.height/width))+x-33
                                                            , get_average_color((0,0), 25, cropped_im)))
            imshow(np.asarray(cropped_im))
            show()

