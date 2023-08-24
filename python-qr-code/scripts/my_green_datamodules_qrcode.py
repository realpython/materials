import segno

qrcode = segno.make_qr("Hello, World")

# Changing only the color of the dark data modules
qrcode.save(
    "my_green_datadark_qrcode.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
)

# Changing the color of the dark and light data modules
qrcode.save(
    "my_green_datamodules_qrcode.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
    data_light="lightgreen",
)
