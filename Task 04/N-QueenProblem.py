print("N-Queen Problem Visualization")

while True:

    n = int(input("Enter board size (4, 5, 6): "))
    val = [' ' for i in range(n*n)]

    def print_board():
        for i in range(n):
            print("+---" * n + "+")
            for j in range(n):
                print("|", end=" ")
                print(val[i*n + j], end=" ")
            print("|")
        print("+---" * n + "+")

    def is_safe(pos):
        r = pos // n
        c = pos % n

        for i in range(n*n):
            if val[i] == 'Q':
                qr = i // n
                qc = i % n

                if qr == r or qc == c:
                    return False

                if abs(qr - r) == abs(qc - c):
                    return False
        return True

    print_board()
    game_over = False

    for x in range(n):
        inp = int(input(f"Enter position for Queen {x+1} (1-{n*n}): "))
        pos = inp - 1

        if pos < 0 or pos >= n*n or not is_safe(pos):
            print(" Invalid position! Game Over.....")
            game_over = True
            break
        else:
            val[pos] = 'Q'
            print_board()

    if not game_over:
        print(" Congratulations... All queens placed safely...")

    ch = input("Do you want to restart? (y/n): ").lower()
    if ch != 'y':
        print("Game Ended.....")
        break
