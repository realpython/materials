import segno

qrcode = segno.make_qr("Hello, World")

# changing only the color of the dark data modules
qrcode.save(
    "my_green_datadark_qrcode.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
)

# changing the color of the dark and light data modules
qrcode.save(
    "my_green_datamodules_qrcode.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
    data_light="lightgreen",
)
