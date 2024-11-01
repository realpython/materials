FROM ubuntu:latest AS free-threaded-builder

# Install dependencies
RUN apt update && \
    apt upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt install -y \
    wget unzip build-essential pkg-config zlib1g-dev python3 clang

# Download Python 3.13 source code
ARG BASE_URL=https://github.com/python/cpython/archive/refs/tags
ARG ZIP_FILE=v3.13.0rc1.zip
RUN wget -P /tmp $BASE_URL/$ZIP_FILE && \
    unzip -d /tmp /tmp/$ZIP_FILE

# Build free-threaded Python 3.13
WORKDIR /tmp/cpython-3.13.0rc1/
RUN ./configure --disable-gil --enable-experimental-jit --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall

FROM free-threaded-builder AS jit-builder

# Build Python 3.13 with JIT only
WORKDIR /tmp/cpython-3.13.0rc1/
RUN make clean && \
    ./configure --enable-experimental-jit --enable-optimizations --prefix=/python3.13-jit && \
    make -j$(nproc) && \
    make install && \
    ln -s /python3.13-jit/bin/python3.13 /usr/local/bin/python3.13j

FROM jit-builder AS stock-builder

# Build stock Python 3.13
WORKDIR /tmp/cpython-3.13.0rc1/
RUN make clean && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make install

FROM ubuntu:latest AS final

COPY --from=jit-builder /python3.13-jit /python3.13-jit
COPY --from=stock-builder /usr/local /usr/local

# Install Python provided by the system
RUN apt update && \
    apt install -y python3 && \
    apt clean && rm -rf /var/lib/apt/lists/*
