import logging
import argparse

import grpc

import image_pb2
import image_pb2_grpc

"""
Your client (in the top level directory, named client) should provide an --input argument 
that specifies the location of a jpeg or png, and an --output argument that specifies the 
path of the output image. It should also provide two arguments that specify which endpoints 
to call on the input image to create the output image. --rotate which takes as argument the 
text form of the rotation enum (EG: NINETY_DEG), and --mean which specifies that the mean 
filter should be run on the input image. You don't need to support multiple of each individual 
argument, but should allow specifying both --rotate and --mean at the same time. 
"""


if __name__ == '__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser(description='Time manipulate images')
    parser.add_argument('--input', nargs='+', help='To be manipulated jpeg or png file(type=string)')
    parser.add_argument('--output', nargs='+', help='To be generated jpeg or png file (type=string)')
    parser.add_argument('--rotate', nargs='+', help='Degress to rotated (type=enum string')
    parser.add_argument('--mean', nargs='+', help='Apply mean filter (type=bool')

