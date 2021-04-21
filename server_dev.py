"""
Your server (in the top level directory, named `server`) should provide a `--port` and `--host` which specify the
port and host the server will bind to.
"""
import logging
import argparse
import threading
from concurrent import futures

import grpc

import image_pb2
import image_pb2_grpc


class Manipulator(image_pb2_grpc.NLImageServiceServicer):

    def MeanFilter(self, request, context):
        return image_pb2.NLImage(message='Manipulating, %s image' % request.image)

    def RotateImage(self, request, context):
        return


def serve(port, host):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_NLImageServiceServicer_to_server(Manipulator(), server)
    server.add_insecure_port(host + ':' + port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser(description='Use grpc to create a server to manipulate images')
    parser.add_argument('--port', type=str, required=True, help='Channel port (e.g. 8000')
    parser.add_argument('--host', type=str, required=True, help='Hostname (e.g. localhost)')
    args = parser.parse_args()
    serve(args.port, args.host)
