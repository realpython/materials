import json
import subprocess
import tempfile
from pathlib import Path

KERNEL = Path("vmlinux").resolve()
ROOTFS = Path("rootfs.ext4").resolve()
BOOT_ARGS = "console=ttyS0 quiet reboot=k panic=1 init=/sbin/run-job"
START, END = "===JOB-START===", "===JOB-END==="


def drive(drive_id, path, is_root):
    return {
        "drive_id": drive_id,
        "path_on_host": str(path),
        "is_root_device": is_root,
        "is_read_only": True,
    }


def run_in_microvm(code, timeout=10):
    with tempfile.TemporaryDirectory() as folder:
        folder = Path(folder)
        (folder / "job").mkdir()
        (folder / "job" / "main.py").write_text(code)
        job_image = folder / "job.ext4"
        subprocess.run(["truncate", "-s", "8M", job_image], check=True)
        subprocess.run(
            ["mkfs.ext4", "-q", "-d", folder / "job", job_image], check=True
        )
        config = {
            "boot-source": {
                "kernel_image_path": str(KERNEL),
                "boot_args": BOOT_ARGS,
            },
            "drives": [
                drive("rootfs", ROOTFS, is_root=True),
                drive("job", job_image, is_root=False),
            ],
            "machine-config": {"vcpu_count": 1, "mem_size_mib": 256},
        }
        config_path = folder / "vm_config.json"
        config_path.write_text(json.dumps(config))
        try:
            result = subprocess.run(
                ["firecracker", "--no-api", "--config-file", config_path],
                capture_output=True,
                text=True,
                errors="replace",
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            return {"exit_code": None, "output": "", "error": "timed out"}
    console = result.stdout.replace("\r\n", "\n")
    if START not in console or END not in console:
        return {"exit_code": None, "output": console, "error": "no job output"}
    output = console.split(START + "\n", 1)[1].split(END, 1)[0]
    exit_code = int(console.split(END, 1)[1].split()[0])
    return {"exit_code": exit_code, "output": output, "error": ""}
