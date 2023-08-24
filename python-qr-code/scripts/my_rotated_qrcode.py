import segno

qrcode = segno.make_qr("Hello, World")

# rotated QR code but truncated
qrcode_rotated = qrcode.to_pil().rotate(45)
qrcode_rotated.save("my_rotated_qrcode.png")

# setting expand to be True
qrcode_rotated = qrcode.to_pil().rotate(45, expand=True)
qrcode_rotated.save("my_rotated_qrcode.png")
