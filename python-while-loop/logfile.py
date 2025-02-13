import time

with open("file.log", mode="r") as file:
    file.seek(0, 2)

    while True:
        line = file.readline()
        if line:
            line_content = line.strip()
            if line_content == "END":
                print("File processing done.")
                break
            print(f"Processing line content: {line_content}")
        else:
            time.sleep(1)
            print("No new content. Retrying in 1 second...")
