import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("scaled_qrcode.png", scale=2)
