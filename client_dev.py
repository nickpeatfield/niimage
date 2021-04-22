"""
Your client (in the top level directory, named client) should provide an --input argument 
that specifies the location of a jpeg or png, and an --output argument that specifies the 
path of the output image. It should also provide two arguments that specify which endpoints 
to call on the input image to create the output image. --rotate which takes as argument the 
text form of the rotation enum (EG: NINETY_DEG), and --mean which specifies that the mean 
filter should be run on the input image. You don't need to support multiple of each individual 
argument, but should allow specifying both --rotate and --mean at the same time. 
"""
import logging
import argparse

import grpc
from PIL import Image

import image_pb2
import image_pb2_grpc

def get_image_formated(img_fp):
    img_pil = Image.open(img_fp)
    img_pil.convert('RBG') # Strip the alpha
    img_bytes = img_pil.tobytes() # TODO work out how this is being represented
    image = image_pb2.NLImage(
        color = True,
        data = img_bytes,
        width = img_pil.width,
        height = img_pil.width
    )
    return image



def run(image_input, output, rotate, mean):
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = image_pb2_grpc.NLImageServiceStub(channel)
        print(f'Lets convert this image to bytes')
        image = get_image_formated(image_input)
        response = stub.RotateImage(image_pb2.NLImageRotateRequest(rotation=rotate, image=image))
    print("Image rotated client received: " + response.NLImage)


if __name__ == '__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser(description='Time manipulate images')
    parser.add_argument('--input', type=str, required=True, help='To be manipulated jpeg or png file(type=string)')
    parser.add_argument('--output', type=str, required=True, help='To be generated jpeg or png file (type=string)')
    parser.add_argument('--rotate', type=str, required=True, help='Degress to rotated (type=enum string')
    parser.add_argument('--mean', type=bool, help='Apply mean filter (type=bool')
    args = parser.parse_args()
    run(args.input, args.output, args.rotate, args.mean)

