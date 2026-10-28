# Python Sandbox: Run Untrusted Code in Docker and MicroVMs

This folder provides the code examples for the Real Python tutorial [Python Sandbox: Run Untrusted Code in Docker and MicroVMs](https://realpython.com/python-sandbox/).

## Prerequisites

- A Linux host (the hostile snippet targets the Linux `/home` folder, and the shell commands assume a POSIX shell). On macOS or Windows, use a Linux virtual machine or WSL 2.
- Python 3.15
- Docker (Podman works too, see the tutorial for the two small changes in `sandbox.py`)
- [RestrictedPython](https://pypi.org/project/RestrictedPython/) 8.5, for `compare.py`
- For `microvm.py` only: the [Firecracker](https://firecracker-microvm.github.io/) binary on your `PATH`, a guest kernel saved as `vmlinux`, and read/write access to `/dev/kvm` (hardware virtualization)

If you run Docker or Podman rootless, make sure your host uses cgroups version 2, or the resource limits are ignored.

## Setup

Create and activate a virtual environment, then install the dependencies:

```console
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

Pull the container image up front so that the first sandboxed run doesn't spend its time budget on a download:

```console
$ docker pull python:3.15-slim
```

## Files

- `sandbox.py`: Defines `run_untrusted()`, which runs code in a locked-down Docker container with no network, a read-only root file system, resource caps, and a wall-clock timeout.
- `compare.py`: Runs the same hostile snippet three ways: `exec()` with restricted builtins, RestrictedPython, and the locked-down container.
- `microvm.py`: Defines `run_in_microvm()`, which runs code inside a Firecracker microVM with its own kernel.
- `rootfs/sbin/run-job`: The shell script that the microVM guest runs instead of an init system.

## Usage

### Docker Sandbox

Import `run_untrusted()` from `sandbox.py`:

```pycon
>>> from sandbox import run_untrusted
>>> run_untrusted("print('Hello from the sandbox')")
```

### Comparing the Three Tiers

Run `compare.py` from the same folder as `sandbox.py`:

```console
(venv) $ python compare.py
```

The first tier leaks your host's `/home` listing, the second refuses to compile the code, and the third shows the container's empty `/home` folder.

### Firecracker MicroVM

First, download a Firecracker release binary and a guest kernel for your CPU architecture by following Firecracker's [getting started guide](https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md). Save the kernel as `vmlinux` in an empty project folder, copy `microvm.py` into it, and make sure your user can read and write `/dev/kvm`.

Then, build the root file system image from the `python:3.15-slim` image inside that project folder. Export the image first, and copy `rootfs/sbin/run-job` from this folder into the exported tree afterward. In the Debian-based image, `/sbin` is a symbolic link to `/usr/sbin`, so exporting on top of an existing `rootfs/sbin/` folder won't work:

```console
$ cid=$(docker create python:3.15-slim)
$ mkdir rootfs/
$ docker export "$cid" | tar -x -C rootfs/
$ docker rm "$cid"
$ mkdir rootfs/job/
$ cp /path/to/python-sandbox/rootfs/sbin/run-job rootfs/sbin/run-job
$ chmod +x rootfs/sbin/run-job
$ truncate -s 300M rootfs.ext4
$ mkfs.ext4 -q -d rootfs/ rootfs.ext4
```

On some distributions, `mkfs.ext4` lives in `/usr/sbin/`, which may not be on a regular user's `PATH`.

With `vmlinux` and `rootfs.ext4` next to `microvm.py`, call `run_in_microvm()`:

```pycon
>>> from microvm import run_in_microvm
>>> run_in_microvm('print("Hello from the microVM")')
{'exit_code': 0, 'output': 'Hello from the microVM\n', 'error': ''}
```
