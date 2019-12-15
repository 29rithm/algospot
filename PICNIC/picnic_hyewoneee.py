def picnic(num, case_list):
    friend_list=[]
    next_list=[]
    result_list = []
    while True:
        if not case_list:
            if num == 2:
                return 1
            return len(result_list)

        for case in case_list:
            compare_list = []
            if not friend_list:
                friend_list.append(case)
            for friend in range(len(friend_list)):
                boolean = True
                if (friend_list[friend][0] not in case) and (friend_list[friend][1] not in case):
                    if case > friend_list[-1]:
                        boolean = False
                    else:
                        boolean = True
                    try_num = friend
                compare_list.append(boolean)
            if compare_list.count(False) == len(compare_list):
                friend_list.append(case)
                if [case[0], case[1]+1] in case_list:
                    next_list.append([case[0], case[1]+1])
        if len(friend_list) * 2 == num:
            if 0 in friend_list[0]:
                result_list.append(friend_list)

        if next_list:
            friend_list = friend_list[0:try_num]
            friend_list.append(next_list[0])
            next_list.pop(0)
            try_num = 0
        else:
            friend_list = []
            next_list = []
            case_list.pop(0)

if __name__ == '__main__':
    import sys
    test_case = sys.stdin.readline()
    case_list = []
    friend_num = 2
    for tc in range(int(test_case)):
        n, m = tuple(map(int, sys.stdin.readline().split()))
        student_list = list(map(int, sys.stdin.readline().split()))
        for i in range((len(student_list) + friend_num - 1) // friend_num):
            set_student = student_list[i * friend_num:(i + 1) * friend_num]
            if set_student[0] < set_student[1]:
                case_list.append([set_student[0], set_student[1]])
            else:
                case_list.append([set_student[1], set_student[0]])
        case_list.sort()
        print(picnic(n, case_list))
