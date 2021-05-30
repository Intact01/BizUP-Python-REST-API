import urllib.parse

from flask import abort
import scipy
import scipy.misc
import scipy.cluster
import binascii
from PIL import Image
from urllib.request import urlopen, pathname2url
import numpy as np


def rgba_to_rgb(img, color=(255, 255, 255)):
    img.load()
    new_img = Image.new('RGB', img.size, color)
    new_img.paste(img, mask=img.split()[3])
    return new_img


def img_from_url(url):
    img = Image.open(urlopen(url))
    if img.mode == "RGBA":
        img = rgba_to_rgb(img)
    return img


def get_dominant_color(arr):
    arr = arr.astype(float)
    # finding clusters
    codes, dist = scipy.cluster.vq.kmeans(arr, 5)

    vecs, dist = scipy.cluster.vq.vq(arr, codes)  # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))  # count occurrences

    index_max = scipy.argmax(counts)  # find most frequent
    peak = codes[index_max]
    color = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    return color, peak


def get_colors(img):
    arr = np.asarray(img)
    shape = arr.shape
    print(shape)
    row_offset = shape[0] // 15
    col_offset = shape[1] // 15
    border_arr = []
    logo_arr = []
    for row in range(shape[0]):
        for col in range(shape[1]):
            if row < row_offset or row >= (shape[0] - row_offset) or col < col_offset or col >= (shape[1] - col_offset):
                border_arr.append((arr[row][col]))
            else:
                logo_arr.append(arr[row][col])
    border, peak_border = get_dominant_color(np.array(border_arr))
    primary, peak_primary = get_dominant_color(np.array(logo_arr))
    print('most frequent border is %s (#%s)' % (peak_border, border))
    print('most frequent  logo is %s (#%s)' % (peak_primary, primary))
    return ("#" + border[:6]).upper(), ("#" + primary[:6]).upper()
