"""
테스트 케이스 수 (C <= 50)

(학생의 수, 친구 쌍의 수)

(0,1), (1,2), (2,3), (3,0), (0,2), (1,3)

1. (0,1), (2,3)
2. (1,2), (3,0)
3. (0,2), (1,3)



0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5


* 학생의 수는 무조건 짝수
* 학생은 2명 이상 10명 이하
"""

def pair_find(students):
    if not students:
        return 1

    target = students.pop(0)
    count = 0

    for student in friends_list[target]:
        if student in students:
            cp_students = students.copy()
            cp_students.remove(student)
            count += pair_find(cp_students)
    return count


if __name__ == '__main__':
    # 여기서 가정은 학생의 숫자는 0부터 10까지 순서대로 있다는 가정
    for _ in range(int(input())):
        friends_cnt = int(input().split()[0])
        friends_set = list(map(int, input().split()))
        friends_list = [[] for _ in range(friends_cnt)]

        for i in range(0, len(friends_set), 2):
            index = friends_set[i]
            value = friends_set[i+1]
            if index > value:
                index, value = value, index
            friends_list[index].append(value)

        print(pair_find(list(range(friends_cnt))))
