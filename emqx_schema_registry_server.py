"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
import logging

import base64
import grpc
import emqx_schema_registry_pb2
import emqx_schema_registry_pb2_grpc

class Parser(emqx_schema_registry_pb2_grpc.ParserServicer):
    def HealthCheck(self, request, context):
        return request
    def Parse(self, request, context):
        if request.type == 1:
            print("parser got encode request: ", request)
            encoded_d = base64.b64encode(request.data)
            return emqx_schema_registry_pb2.ParseResponse(code='SUCCESS', message="ok",
                result=encoded_d)
        elif request.type == 0:
            print("parser got decode request: ", request)
            decoded_d = base64.b64decode(request.data)
            return emqx_schema_registry_pb2.ParseResponse(code='SUCCESS', message="ok",
                result=decoded_d)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    emqx_schema_registry_pb2_grpc.add_ParserServicer_to_server(
        Parser(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()

