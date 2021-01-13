from cv2 import *
from numpy import array, where, ones_like
from matplotlib import pyplot


# 画像を白黒で読み込む
img_bw = imread('tapioca_drink.jpg', 2) # ,2は白黒で読み込む合図

# 一定の明るさ(この場合は120)より暗い部分のみ残してみる
img_mod = where(img_bw > 120 , 0, img_bw)
pyplot.imshow(img_mod)