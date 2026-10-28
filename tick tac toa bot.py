# Learning data for each square
data = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def training(map, data):

    # Horizontal checks
    for d in range(len(map)):
        for dd in range(len(map[d]) - 1):

            if map[d][dd] == "O" and map[d][dd + 1] == "O":
                data[d][dd] += 1
                data[d][dd + 1] += 1
            else:
                data[d][dd] -= 1
                data[d][dd + 1] -= 1

    # Vertical checks
    for d in range(len(map) - 1):
        for dd in range(len(map[d])):

            if map[d][dd] == "O" and map[d + 1][dd] == "O":
                data[d][dd] += 1
                data[d + 1][dd] += 1
            else:
                data[d][dd] -= 1
                data[d + 1][dd] -= 1

    # Main diagonal
    for d in range(len(map) - 1):

        if map[d][d] == "O" and map[d + 1][d + 1] == "O":
            data[d][d] += 1
            data[d + 1][d + 1] += 1
        else:
            data[d][d] -= 1
            data[d + 1][d + 1] -= 1

    # Other diagonal
    for d in range(len(map) - 1):

        if map[d][2 - d] == "O" and map[d + 1][1 - d] == "O":
            data[d][2 - d] += 1
            data[d + 1][1 - d] += 1
        else:
            data[d][2 - d] -= 1
            data[d + 1][1 - d] -= 1

    return data


def your_go(map, possible):

    decision = -1

    while decision not in possible:
        decision = input("Pick where you want to go (1-9): ")

        try:
            decision = int(decision)-1
        except:
            decision = -1

    possible.remove(decision)

    map[decision // 3][decision % 3] = "X"

    return map, possible


def bot_go(map, possible, data):

    lines = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],

        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],

        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]

    # WIN IF POSSIBLE
    for line in lines:

        values = [map[r][c] for r, c in line]

        if values.count("O") == 2 and values.count(" ") == 1:

            for r, c in line:

                if map[r][c] == " ":

                    decision = r * 3 + c

                    possible.remove(decision)
                    map[r][c] = "O"

                    return map, possible

    # BLOCK PLAYER
    for line in lines:

        values = [map[r][c] for r, c in line]

        if values.count("X") == 2 and values.count(" ") == 1:

            for r, c in line:

                if map[r][c] == " ":

                    decision = r * 3 + c

                    possible.remove(decision)
                    map[r][c] = "O"

                    return map, possible

    # LEARNED MOVE
    best_score = -999999
    decision = possible[0]

    for pos in possible:

        score = data[pos // 3][pos % 3]

        if score > best_score:
            best_score = score
            decision = pos

    possible.remove(decision)
    map[decision // 3][decision % 3] = "O"

    return map, possible


def check_winner(map):

    # Rows
    for row in range(3):

        if map[row] == ["X", "X", "X"]:
            return "X"

        if map[row] == ["O", "O", "O"]:
            return "O"

    # Columns
    for col in range(3):

        if map[0][col] == map[1][col] == map[2][col] == "X":
            return "X"

        if map[0][col] == map[1][col] == map[2][col] == "O":
            return "O"

    # Diagonals
    if map[0][0] == map[1][1] == map[2][2]:
        if map[0][0] != " ":
            return map[0][0]

    if map[0][2] == map[1][1] == map[2][0]:
        if map[0][2] != " ":
            return map[0][2]

    return None


def actuall_game_loop(possible, map, data, go):

    while len(possible) > 0:

        print(
            "\n"
            f" {map[0][0]} | {map[0][1]} | {map[0][2]}\n"
            "---+---+---\n"
            f" {map[1][0]} | {map[1][1]} | {map[1][2]}\n"
            "---+---+---\n"
            f" {map[2][0]} | {map[2][1]} | {map[2][2]}\n"
        )

        if go == 1:
            map, possible = your_go(map, possible)
        else:
            map, possible = bot_go(map, possible, data)

        winner = check_winner(map)

        if winner is not None:
            print(winner + " wins")
            break

        if len(possible) == 0:
            print("Draw")
            break

        go += 1

        if go == 3:
            go = 1

    print(
        "\n"
        f" {map[0][0]} | {map[0][1]} | {map[0][2]}\n"
        "---+---+---\n"
        f" {map[1][0]} | {map[1][1]} | {map[1][2]}\n"
        "---+---+---\n"
        f" {map[2][0]} | {map[2][1]} | {map[2][2]}\n"
    )

    data = training(map, data)

    decision = input("Do you want to play again (y/n)? ")

    if decision.lower() == "y":

        new_map = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        new_possible = list(range(9))

        return actuall_game_loop(new_possible, new_map, data, 1)

    else:

        print("\nBot learning data:")

        print(
            f"{data[0][0]} | {data[0][1]} | {data[0][2]}\n"
            "---+---+---\n"
            f"{data[1][0]} | {data[1][1]} | {data[1][2]}\n"
            "---+---+---\n"
            f"{data[2][0]} | {data[2][1]} | {data[2][2]}"
        )

        print("end")


map = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

possible = list(range(9))


actuall_game_loop(possible, map, data, 1)