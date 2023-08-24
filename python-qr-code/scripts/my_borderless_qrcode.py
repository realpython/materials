import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("my_borderless_qrcode.png", scale=5, border=0)
