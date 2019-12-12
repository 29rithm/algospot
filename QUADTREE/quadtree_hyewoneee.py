def QuadList(data_list):
    set_list = []
    while True:
        try:
            char = next(data_list)
            if char == 'x':
                set_list.append(QuadList(data_list))
            else:
                set_list.append(char)
            if len(set_list) == 4:
                return set_list
        except StopIteration:
            return set_list[0]

def QuadTree(data):
    if len(data) == 1:
        print(data[0])
    tree_list = data
    for i in range(len(data)):
        if isinstance(data[i], list):
            tree_list[i] = QuadTree(data[i])
    return 'x' + data[2] + data[3] + data[0] + data[1]

if __name__ == '__main__':
    import sys
    case = sys.stdin.readline()
    if int(case) > 50:
        raise print('테스트 케이스는 50번을 넘길 수 없다.')
    for tc in range(int(case)):
        quad_list = []
        input_list = input()
        if input_list == 'w' or input_list == 'b':
            print(input_list)
        else:
            for i in input_list:
                quad_list.append(i)
            print(QuadTree(QuadList(iter(quad_list))))
