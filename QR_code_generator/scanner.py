import qrcode as qr
from PIL import Image

# image = qr.make("https://pypi.org/")      # Add the url or data you want to make the qr code of.
# image.save("test.png")                    # This will save the qr code with the desired extension of image

qr_code = qr.QRCode(version=1,
                    error_correction = qr.constants.ERROR_CORRECT_H,            # This will help to prevent qr code to throw error while scanning
                    box_size=10,border=4)                                       

qr_code.add_data("https://github.com/Raj3019")
qr_code.make(fit=True)                                                          # This means that the qr will only generate if all the requriments meet
img = qr_code.make_image(fill_color="blue", back_color="white")                 # Color of qr code and background color 
img.save("test2.png")