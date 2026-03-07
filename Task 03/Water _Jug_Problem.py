def dfs(state, visited, path):
    x, y = state

    if x == 2 or y == 2:
        print("\nSolution Steps:")
        for step in path:
            print(step)
        print("Goal Reached:", state)
        return True

    if state in visited:
        return False

    visited.add(state)

    # All possible moves with rules
    moves = [
        ((4, y), "Fill 4L Jug"),
        ((x, 3), "Fill 3L Jug"),
        ((0, y), "Empty 4L Jug"),
        ((x, 0), "Empty 3L Jug"),
        ((x - min(x, 3 - y), y + min(x, 3 - y)), "Pour 4L → 3L"),
        ((x + min(y, 4 - x), y - min(y, 4 - x)), "Pour 3L → 4L")
    ]

    for next_state, rule in moves:
        if dfs(next_state, visited, path + [f"{rule} → {next_state}"]):
            return True

    return False


visited = set()
dfs((0, 0), visited, [])
