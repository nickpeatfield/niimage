#!/usr/bin/env python
import logging
import argparse
import threading
from concurrent import futures

import grpc
from PIL import Image, ImageFilter

import image_pb2
import image_pb2_grpc


def mean_filter(img):
    """Returns a pixel box blured image rad1 so just nearest"""
    if img.color:
        image = Image.frombytes('RGB', data=img.data, size=(img.width, img.height))
    else:
        image = Image.frombytes('L', data=img.data, size=(img.width, img.height))
    image_nearest = image.filter(filter=ImageFilter.BoxBlur(1))
    img.width = image_nearest.width
    img.height = image_nearest.height
    img.data = image_nearest.tobytes()
    return img

def rotate_image(img, rotation):
    """Returns rotated image"""
    if img.color:
        image = Image.frombytes('RGB',data=img.data, size=(img.width, img.height))
    else:
        image = Image.frombytes('L', data=img.data, size=(img.width, img.height))
    image_rotated = image.rotate(rotation * 90, expand=1)
    img.width = image_rotated.width
    img.height = image_rotated.height
    img.data = image_rotated.tobytes()
    return img


class NLImageServiceServicer(image_pb2_grpc.NLImageServiceServicer):

    def MeanFilter(self, request, context):
        image = mean_filter(request)
        return image

    def RotateImage(self, request, context):
        image = rotate_image(request.image, request.rotation)
        return image


def serve(port, host):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    image_pb2_grpc.add_NLImageServiceServicer_to_server(NLImageServiceServicer(), server)
    server.add_insecure_port(host + ':' + port)
    server.start()
    print(f'Server is running at {host}:{port}')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser(description='Use grpc to create a server to manipulate images')
    parser.add_argument('--port', type=str, required=True, help='Channel port (e.g. 8000')
    parser.add_argument('--host', type=str, required=True, help='Hostname (e.g. localhost)')
    args = parser.parse_args()
    serve(args.port, args.host)
