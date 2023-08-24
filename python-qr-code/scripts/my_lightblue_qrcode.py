import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("my_lightblue_qrcode.png", light="lightblue", scale=5)
