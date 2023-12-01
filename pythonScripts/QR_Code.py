# pip install PyQRCode
# pip install pypng

import pyqrcode
import png

s = "https://github.com/yshashanky/miniProjects" # link to which QR code will redirect

url = pyqrcode.create(s) # create QA Code

url.svg('myqr.svg', scale=8) # create and save svg image of generated QR Code
url.png('myqr.png', scale=8) # create and save jpg image of generated QR Code
url.show() # shows the created png image

# more comples method to create QR code
# big_code = pyqrcode.create('https://github.com/yshashanky/miniProjects', error='L', version=27, mode='binary')
# big_code.png('code.png', scale=10, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
# big_code.show()