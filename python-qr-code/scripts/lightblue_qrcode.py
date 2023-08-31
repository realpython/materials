import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("lightblue_qrcode.png", light="lightblue", scale=5)
