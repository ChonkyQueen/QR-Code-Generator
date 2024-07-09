import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code, higher the number bigger the code image and complicated picture
    box_size = 10, #size of the box where the qr code will be displayed
    border = 5 #white part of the image -- border above in all 4 sides with white colour
)

data = "https://cdn.britannica.com/35/233235-050-8DED07E3/Pug-dog.jpg"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white")
img.save("test.png")