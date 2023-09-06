import segno

qrcode = segno.make_qr("Hello, World")

# Rotated QR code but truncated
qrcode_rotated = qrcode.to_pil().rotate(45)
qrcode_rotated.save("rotated_qrcode.png")

# Setting expand to True
qrcode_rotated = qrcode.to_pil().rotate(45, expand=True)
qrcode_rotated.save("rotated_qrcode.png")
