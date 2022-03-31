import subprocess

process = subprocess.run(
    ["python", "random_num_gen.py"], capture_output=True, text=True
)

print(int(process.stdout))
