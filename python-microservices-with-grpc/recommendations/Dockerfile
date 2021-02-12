# syntax = docker/dockerfile:1.0-experimental
# DOCKER_BUILDKIT=1 docker build . -f recommendations/Dockerfile -t recommendations --secret id=ca.key,src=ca.key

FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/
COPY ca.pem /service/recommendations/

WORKDIR /service/recommendations
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto
RUN openssl req -nodes -newkey rsa:4096 -subj /CN=recommendations \
                -keyout server.key -out server.csr
RUN --mount=type=secret,id=ca.key \
    openssl x509 -req -in server.csr -CA ca.pem -CAkey /run/secrets/ca.key \
                 -set_serial 1 -out server.pem

EXPOSE 50051
ENTRYPOINT [ "python", "recommendations.py" ]
