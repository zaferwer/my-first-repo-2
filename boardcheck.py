def f_word(board, word):
    def check_adj(r, c, pos, visited):
        if not (
            r >= 0
            and r < len(board)
            and c >= 0
            and c < len(board[0])
            and pos < len(word)
        ):
            return False
        if (r, c) in visited:
            return False
        if board[r][c] != word[pos]:
            return False
        if pos == len(word) - 1:
            return True
        visited.add((r, c))
        for i in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            if check_adj(r + i[0], c + i[1], pos + 1, visited):
                return True
        visited.remove((r, c))
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == word[0]:
                if check_adj(r, c, 0, set()):
                    return True
    return False


def exists(x_list, letter):
    x = []
    for i in range(len(x_list)):
        for j in range(len(x_list[0])):
            x.append(x_list[i][j])
    print(x)
    for k in range(len(letter) - 1):
        # for t in range(letter.count(letter[k])):
        if (
            (x.index(letter[k]) + 1 == x.index(letter[k + 1]))
            or (x.index(letter[k]) - 1 == x.index(letter[k + 1]))
            or (x.index(letter[k]) + 4 == x.index(letter[k + 1]))
            or (x.index(letter[k]) - 4 == x.index(letter[k + 1]))
        ):
            result = True
        # if letter[k]==letter[k+1]:

        else:
            result = False
            break
    print(result)


x_list = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
exists(x_list, "SC")
