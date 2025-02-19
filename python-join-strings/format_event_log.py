import json


def load_log_file(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        return json.load(file)


def format_event_log(event_log):
    lines = []
    for timestamp, events in event_log.items():
        # Convert the events list to a string separated by commas
        event_list_str = ", ".join(events)
        # Create a single line string
        line = f"{timestamp} => {event_list_str}"
        lines.append(line)

    # Join all lines with a newline separator
    return "\n".join(lines)


if __name__ == "__main__":
    log_file_path = "event_log.json"
    event_log = load_log_file(log_file_path)
    output = format_event_log(event_log)
    print(output)
