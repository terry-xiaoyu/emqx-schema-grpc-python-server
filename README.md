# emqx-schema-grpc-python-server

This is a demo gRPC server for the [emqx schema registry](https://docs.emqx.com/en/enterprise/v4.4/rule/schema-registry.html).

It parse 

## Prerequisites

- [Python](https://www.python.org) 3.5 or higher
- pip version 9.0.1 or higher

## Run

Install gRPC and gRPC Tools:

```
pip3 install grpcio
pip3 install grpcio-tools
```
Try to compile the `*.proto` files:

```
python3 -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/emqx_schema_registry.proto
```

Run server:

```
python emqx_schema_registry_server.py
```
