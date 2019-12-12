def matching_friend(students, already=0):
    global estimate_count
    global friendship

    for first in students:
        if first < already:
            continue

        for second in students:
            if first >= second:
                continue

            if (first, second) in friendship:
                remain_students = students[:]
                remain_students.remove(first)
                remain_students.remove(second)

                if len(remain_students) > 0:
                    matching_friend(remain_students, first)
                else:
                    estimate_count += 1


if __name__ == "__main__":
    import sys
    for tc in range(int(sys.stdin.readline())):
        # 표준 입력 처리
        n, m = tuple(map(int, sys.stdin.readline().split()))
        friendship_list = list(map(int, sys.stdin.readline().split()))
        friendship_list_odd = [friendship_list[x] for x in range(0, len(friendship_list), 2)]
        friendship_list_even = [friendship_list[x] for x in range(1, len(friendship_list), 2)]
        friendship = [tuple(sorted(x)) for x in zip(friendship_list_odd, friendship_list_even)]

        # 경우의 수(전역 변수)
        estimate_count = 0

        # 메인 함수
        matching_friend(list(range(n)))

        # 결과 출력
        print(estimate_count)
