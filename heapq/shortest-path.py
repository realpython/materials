import heapq


map = """\
.......X..
.......X..
....XXXX..
..........
..........
"""


def parse_map(map):
    lines = map.splitlines()
    origin = 0, 0
    destination = len(lines[0]) - 1, len(lines) - 1
    return lines, origin, destination


def is_valid(lines, position):
    x, y = position
    if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
        return False
    if lines[y][x] == "X":
        return False
    return True


def get_neighbors(lines, current):
    x, y = current
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            position = x + dx, y + dy
            if is_valid(lines, position):
                yield position


def get_shorter_paths(tentative, positions, through):
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):
            continue
        yield position, path


def find_path(map):
    lines, origin, destination = parse_map(map)
    tentative = {origin: []}
    candidates = [(0, origin)]
    known = set()
    while destination not in known:
        if not candidates:
            raise ValueError("no path")
        _ignored, current = heapq.heappop(candidates)
        if current in known:
            continue
        neighbors = set(get_neighbors(lines, current)) - known
        relevant_neighbors = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in relevant_neighbors:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))
        known.add(current)
    return tentative[destination] + [destination]


def show_path(path, map):
    lines = map.splitlines()
    for x, y in path:
        lines[y] = lines[y][:x] + "@" + lines[y][x + 1 :]
    return "\n".join(lines) + "\n"


path = find_path(map)
print(show_path(path, map))
