from PIL import Image
import numpy as np


def bw_convert():
    a = Image.open("4_pict.jpg")
    b = np.asarray(a)
    c = np.array((0.2989, 0.5870, 0.1140))
    bw = np.round(np.sum(b * c, axis=2))
    Image.fromarray(bw).convert("RGB").save("4_pict_bw.jpg")


bw_convert()
