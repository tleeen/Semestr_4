with open("10_pct.bmp", "rb") as bmp_image:
    data = list(bytes(bmp_image.read()))

a = []
for count, byte in enumerate(data):
    if count > 54:
        a.append(255 - byte)
    else:
        a.append(byte)

with open("10_pct_res.bmp", "wb") as bmp_image:
    bmp_image.write(bytes(a))
