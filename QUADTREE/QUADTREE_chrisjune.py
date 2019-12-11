# QUADTREE
# 실질적으로 자리를 바꾸는 문제임
# x1234 -> x3412형태
# x12x12344 -> xx3412412
# 가장 작은 형태인 x1234를 뒤집어서 반환하게한다

string = []


def flip():
    # 첫번째 요소를 검사
    first = string.pop(0)
    swap = []
    # x 가 아니면 그대로 반환
    if first != 'x':
        return first

    # x로 시작하면 쿼드가 필요하므로 반복문으로 요소를 삽입한다
    swap.append(first)
    for i in range(0, len(string)):
        # 어디까지 부분인지 모르기 때문에 swap에 넣은 개수가 x1234의 형태로 차게되면 반복을 끝내고 call stack을 빠져나가도록 한다
        if len(swap) == 5:
            break

        # 만약 1234라고 생각한 요소에서 x가 다시 등장하면 부분문제가 되므로 재귀를 호출한다
        target = string.pop(0)
        if target == 'x':
            # 재귀 함수로 들어갈때 1234가 아닌 x1234로 형태로 반환받아야하기 때문에 x를 다시 붙여서 호출한다
            string.insert(0, target)
            # 재귀 결과또한 1234중 하나의 요소에 해당하므로 swap에 추가해준다
            swap.append(flip())
        else:
            # 1234에서 숫자에 해당하므로 swap에 추가
            swap.append(target)
    # 모든 요소가 다 찼기 때문에 자리를 바꿔준다
    swap[1], swap[2], swap[3], swap[4] = swap[3], swap[4], swap[1], swap[2]
    return swap


result = []


# Nested한 리스트를 flat하게 변경해준다
# [[[x,1,2,3,4],2,3,4],2,3,4] -> [x,1,2,3,4,2,3,4,2,3,4]
def convert_to_list(li):
    for i in li:
        if isinstance(i, list):
            convert_to_list(i)
        else:
            result.append(i)


if __name__ == '__main__':
    for case in range(int(input())):
        string = list(input())
        convert_to_list(flip())
        print(''.join(result))
        result = []
