from pytesser import * 
from PIL import Image
file = open("code.text", "w")


im = Image.open('image.png')
text = image_to_string(im)
file.write(text.replace(" ",""))
file.close()
