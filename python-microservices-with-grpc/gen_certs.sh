#!/bin/bash

# Generate CA key and self-signed cert
openssl req -x509 -nodes -newkey rsa:4096 -keyout ca.key -out ca.pem -subj /O=me

# Generate a private key and certificate signing request for the client and server
openssl req -nodes -newkey rsa:4096 -keyout client.key -out client.csr -subj /CN=marketplace
openssl req -nodes -newkey rsa:4096 -keyout server.key -out server.csr -subj /CN=recommendations

# Sign the client and server certs with the CA cert
openssl x509 -req -in client.csr -CA ca.pem -CAkey ca.key -set_serial 1 -out client.pem
openssl x509 -req -in server.csr -CA ca.pem -CAkey ca.key -set_serial 1 -out server.pem
