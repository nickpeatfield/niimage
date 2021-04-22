import argparse
import os

import numpy as np
from PIL import Image, ImageFilter


def do_image_rotate(img_in,img_out):
    image = Image.open(img_in)
    out = image.rotate(45)
    out.save(img_out)


def do_image_mean(img_in,img_out):
    image = Image.open(img_in)
    image_nearest = image.filter(filter=ImageFilter.BoxBlur(1))
    image_nearest.save(img_out)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Just dev zone')
    parser.add_argument('--input', type=str, required=True, help='Channel port (e.g. 8000')
    parser.add_argument('--output', type=str, required=True, help='Hostname (e.g. localhost)')
    args = parser.parse_args()
    do_image_rotate(args.input, args.output)
    do_image_mean(args.input, args.output)