import segno

qrcode = segno.make_qr("Hello, World")

# without changing the color of the quiet zone
qrcode.save("my_darkblue_qrcode.png", scale=5, dark="darkblue")

# with quiet zone
qrcode.save(
    "my_darkblue_qrcode.png", scale=5, dark="darkblue", quiet_zone="maroon"
)
