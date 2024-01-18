import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,                                             #version parameter ranges from int values 1 to 40 that controls the size of the QR 
                 error_correction=qrcode.constants.ERROR_CORRECT_H,     # erorr correcton has 4 times: 1) L:<=7%eroor correction, M:<=15%, Q:<=25%, H<=30%
                box_size=10,                                           # box_size - how many pixcels 
                border=4)                                               # border: how many boxes thick the border should be (the default is 4, which is the minimum in the specification).
qr.add_data("https://web.whatsapp.com/")                       #one can add in text, links, payment links in the method make_image to create respective QR code.
qr.make(fit=True)
img=qr.make_image(fill_color="purple",back_color="white")
img.save("c:/Users/manas/OneDrive/Desktop/coding/.vscode/python/ggqr.png")  #give the complete path if you want it to be stored in a particular location on your desktop.
# if the complete path is not given, the png file would just appear on your project file .
# one can change the colors and other attributes as per the requirement .
#add_data(): This method is used to add data to the QRCode object. It takes the data to be encoded as a parameter.
#make(): with (fit=True) ensures that the entire dimension of the QR Code is utilized.
