import logging
import argparse

import grpc
from PIL import Image

import image_pb2
import image_pb2_grpc


def get_image_formated(img_fp):
    img_pil = Image.open(img_fp)
    if img_pil.mode == 'RGBA':  # strip the alpha
        img_pil = img_pil.convert('RGB')
    img_bytes = img_pil.tobytes()  # TODO work out how this is being represented
    image = image_pb2.NLImage(
        color=True,
        data=img_bytes,
        width=img_pil.width,
        height=img_pil.height
    )
    return image


def save_image(img, img_output):
    if img.color:
        image = Image.frombytes('RGB', data=img.data, size=(img.width, img.height))
    else:
        image = Image.frombytes('L', data=img.data, size=(img.width, img.height))
    image.save(img_output, 'PNG')
    return image


def run(image_input, output, rotate, mean):
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = image_pb2_grpc.NLImageServiceStub(channel)
        print(f'Lets convert this image to bytes')
        image = get_image_formated(image_input)
        print(f'Lets mean the image')
        if mean:
            image = stub.MeanFilter(image_pb2.NLImage(data=image.data, color=image.color, width=image.width,
                                                      height=image.height))
        print(f'Lets rotate the image and because of conditionals we can save')
        image = stub.RotateImage(image_pb2.NLImageRotateRequest(rotation=rotate, image=image))
        save_image(image, output)
        print(f"Image was saved at location {output}")


if __name__ == '__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser(prog='client', description='Time manipulate images')
    parser.add_argument('--input', type=str, required=True, help='To be manipulated jpeg or png file(type=string)')
    parser.add_argument('--output', type=str, required=True, help='To be generated jpeg or png file (type=string)')
    parser.add_argument('--rotate', type=str, required=True, help='Degress to rotate ')
    parser.add_argument('--mean', action='store_true', help='Apply mean filter (type=bool)')
    args = parser.parse_args()
    run(args.input, args.output, args.rotate, args.mean)
