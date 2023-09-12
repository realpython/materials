import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("borderless_qrcode.png", scale=5, border=0)
