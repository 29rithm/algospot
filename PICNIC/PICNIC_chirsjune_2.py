# 1. 두명씩 짝을 짓는다
# 2. 친구여부를 확인하고 짝을 지어준다.
# 3. 일부만 짝이 아니어도 다른 방법으로 판단한다

# 친구:1,2,3,4  / 짝: (1,2), (3,4) 와 (2,1), (3,4)는 동일하다
# 차이는 친구를 맺어줄때
# 중복없이 짝을 맺는 방법은 받은 친구리스트에서 제일 작은 번호를 뽑고
# 나머지 친구들을 for로 친구를 맺어준다. 그리고 나머지 친구리스트는 재귀호출

pairs = []

def count_pair(students):
    if not students:
        return 1
    first = students[0]
    other = students[1:]

    count = 0
    for idx in range(len(other)):
        pair = other.pop(idx)

        # 친구 관계이면 재귀태우고 아니면 바로 롤백
        if [first, pair] in pairs:
            count += count_pair(other)
        other.insert(idx, pair)
    return count

if __name__ == '__main__':
    for case in range(int(input())):
        info = input().split()
        students = int(info[0])

        pair_input = input().split()
        pairs = [sorted([int(pair_input[i]), int(pair_input[i+1])]) for i in range(0, len(pair_input), 2)]
        print(count_pair([i for i in range(students)]))


