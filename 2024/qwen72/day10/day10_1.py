def parse_input(filename):
    with open(filename, 'r') as file:
        map = [list(map(int, line.strip())) for line in file]
    return map

def find_trailheads(map):
    trailheads = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(map, x, y, current_height):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return False
    if map[x][y] != current_height + 1:
        return False
    return True

def explore_trail(map, x, y, target_height, visited):
    if map[x][y] == target_height:
        return 1
    if map[x][y] == 9:
        return 0
    visited.add((x, y))
    current_height = map[x][y]
    reachable = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in visited and is_valid_move(map, nx, ny, current_height):
            reachable += explore_trail(map, nx, ny, target_height, visited)
    return reachable

def calculate_score(map, trailhead):
    x, y = trailhead
    visited = set()
    return explore_trail(map, x, y, 9, visited)

def sum_of_scores(map):
    trailheads = find_trailheads(map)
    total_score = 0
    for trailhead in trailheads:
        total_score += calculate_score(map, trailhead)
    return total_score

def main():
    map = parse_input('input.txt')
    total_score = sum_of_scores(map)
    print(f"The sum of the scores of all trailheads is: {total_score}")

if __name__ == "__main__":
    main()