import qrcode

data = input("Text or URL: ")
filename = input("File name: ")
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print("QR code generated as " + filename)

#venv\Scripts\activate for activating
#python QR.py for running
#deactivate for deactivating