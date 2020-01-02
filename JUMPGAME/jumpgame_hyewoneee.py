def JumpGame(i, j):
    if i == int(game_count)-1 and j == int(game_count) -1:
        return True
    if i > int(game_count) -1 or j > int(game_count) -1:
        return False
    if ret[i][j] == -1:
        return False
    game = game_list[i][j]
    ret[i][j] = -1

    return JumpGame(i, game+j ) or JumpGame(i+game, j)

if __name__ == '__main__':
    import sys
    case = sys.stdin.readline()

    if int(case) > 50:
        raise print('테스트 케이스는 50번을 넘길 수 없다.')

    for tc in range(int(case)):
        game_list = []
        ret = []
        game_count = input()
        for count in range(int(game_count)):
            game_list.append([int(i) for i in input().split(' ')])
            ret.append([0] * int(game_count))

        print('YES' if JumpGame(0,0) else 'NO')
