import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("my_scaled_qrcode.png", scale=2)
