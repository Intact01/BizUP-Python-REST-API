from urllib.error import URLError
from flask import abort
import scipy
import scipy.misc
import scipy.cluster
import binascii
from PIL import Image, UnidentifiedImageError
from urllib.request import urlopen
import numpy as np


# get PIL.Image.Image from url
def img_from_url(url):
    try:
        img = Image.open(urlopen(url))
    except URLError:
        abort(404, "Invalid URL")
    except UnidentifiedImageError:
        abort(404, "Image not found")
    return img


# get dominant color in the RGB/RGBA array of pixels
def get_dominant_color(arr):
    arr = arr.astype(float)
    codes, distort = scipy.cluster.vq.kmeans(arr, 5)        # finding clusters
    code_indices, distort = scipy.cluster.vq.vq(arr, codes)  # assign codes
    counts, bins = np.histogram(code_indices, len(codes))   # count occurrences
    index_max = np.argmax(counts)  # find most frequent
    peak = codes[index_max]
    color = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    return color


# get border color and logo primary color from PIL.Image.Image
def get_colors(img):
    arr = np.asarray(img)
    shape = arr.shape
    # separate border pixels from others
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
    # get dominant colors in both set of pixels
    border = get_dominant_color(np.array(border_arr))
    primary = get_dominant_color(np.array(logo_arr))
    return ("#" + border[:6]).upper(), ("#" + primary[:6]).upper()
