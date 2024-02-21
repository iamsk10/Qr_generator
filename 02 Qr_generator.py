import qrcode
import image
qr =qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
# user input there number
data = input('enter your message to convert qr : ')

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color = "white")
# save the qr in image formate
img.save("twono.png")
