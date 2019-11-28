pair_list = None

def count_pairs(students, pair):
    # [0, 1, 2, 3]
    if len(pair) == 2:
        print('pair',pair)
        checked = is_friend(pair, pair_list)
        if not checked:
            pair.clear()
            return 0
        if checked:
            pair.clear()

    if not students:
        return 1

    count = 0

    for i in range(len(students)):
        student = students.pop(i)
        pair.append(student)

        count += count_pairs(students, pair)
        students.insert(i, student)
    return count

def is_friend(pair, pair_list):
    # pair [0, 1]
    # pair_list [0,1,1,2,2,3,3,0,0,2,1,3]
    for i in range(0, len(pair_list),2):
        if (pair[0], pair[1]) == (pair_list[i], pair_list[i+1]) or\
                (pair[0], pair[1]) == (pair_list[i+1], pair_list[i]):
            return True
    return False

# Main
if __name__ == '__main__':
    # for case in range(int(input())):
    for case in range(1):
        # info = list(map(int, input().split()))
        info = [4, 6]
        # info = [6, 10]
        # 4
        students_count = info[0]
        students = [i for i in range(students_count)]
        # 6
        pair_count = info[1]
        # 0 1 1 2 2 3 3 0 0 2 1 3
        # pair_list = list(map(int, input().split()))
        # pair_list = [0,1,1,2,2,3,3,0,0,2,1,3]
        pair_list = [0,1,2,3]
        # pair_list = [0,1, 0,2, 1,2, 1,3, 1,4, 2,3, 2,4, 3,4, 3,5, 4,5]
        print(count_pairs(students, []))
