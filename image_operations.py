import urllib.parse

import numpy
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
    # finding clusters
    codes, dist = scipy.cluster.vq.kmeans(arr, 5)
    # print('cluster centres:\n', codes)

    vecs, dist = scipy.cluster.vq.vq(arr, codes)  # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))  # count occurrences

    index_max = scipy.argmax(counts)  # find most frequent
    peak = codes[index_max]
    color = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    return color, peak

def get_border_color(img):
    arr = np.asarray(img)
    shape = arr.shape
    print(shape)
    row_offset = shape[0] // 10
    col_offset = shape[1] // 10
    border_arr = []
    for row in range(shape[0]):
        for col in range(shape[1]):
            if row < row_offset or row >= (shape[0] - row_offset) or col < col_offset or col >= (shape[1] - col_offset):
                border_arr.append((arr[row][col]))
    border_arr = np.array(border_arr)
    border_shape = border_arr.shape
    border_arr = border_arr.reshape(border_shape).astype(float)
    color, peak = get_dominant_color(border_arr)
    print('most frequent is %s (#%s)' % (peak, color))
    return "#" + color[:6]


def get_primary_color(img):
    arr = np.asarray(img)
    shape = arr.shape
    print(shape)
    arr = arr.reshape(scipy.product(shape[:2]), shape[2]).astype(float)
    color, peak = get_dominant_color(arr)
    print('most frequent is %s (#%s)' % (peak, color))
    return "#" + color[:6]

# def remove_background(img)
