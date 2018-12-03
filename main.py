'''
For each bar line:

detect lines in image using hough

'''
import numpy as np
from PIL import Image
from PIL import ImageFilter

import sys



class Note:
    def __init__(self, note, length):
        self.note = note
        self.length = length

class Line:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Cleff:
    def __init__(self,t="treble"):
        self.lines = []
        self.t = t

class Bar:
    def __init__(self):
        self.cleffs = []

class Song:
    def __init__(self, cleffs):
        self.cleffs = cleffs

def dectectKey():
    pass

def preProcess(img):
    # small gaussian filter
    # 
    pass

def toBinary(im,thresh):
    f = lambda v: 0 if v > thresh else 255
    return im.point(f)

def main():
    path = sys.argv[1]
    im = Image.open(path).convert('1')
    blurred = im.filter(ImageFilter.GaussianBlur(radius=1))
    im.show()
    blurred.show()


if __name__== "__main__":
    main()