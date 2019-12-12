# QUADTREE
# 실질적으로 자리를 바꾸는 문제임
# x1234 -> x3412형태
# x12x12344 -> xx3412412
# 가장 작은 형태인 x1234를 뒤집어서 반환하게한다


string = None
recursived = False


def flip():
    # 재귀로 시작한 것인지 판단하기 위한 변수
    global recursived
    if recursived:
        first = 'x'
        recursived = False
    else:
        # 재귀로 시작한게 아니라면 입력 문자열에서 첫번째를 읽는다
        first = next(string)

    # 만약 첫 문자가 x로 시작하지 않으면 볼 필요없이 그대로반환
    if first != 'x':
        return first

    # 여기서부턴 x1234의 형태가 된다
    # x도 결과문자에 포함해야하기 때문에 append
    swap = []
    swap.append(first)
    try:
        while True:
            # 입력받은 문자열이 얼마나 긴지 모르기 때문에 판단여부를 swap할 대상리스트가
            # 총 [x,1,2,3,4] 5개가 되면 끝낸다
            if len(swap) == 5:
                break

            # 여기선 x 이후의 문자가 되는데
            # 다시 x가 등장하면 재귀를 호출하여 부분문제를 풀도록하고
            # 숫자가 등장하면 x,1,2,3,4의 문자열이기 때문에 swap에 모두 넣어준다
            target = next(string)
            if target == 'x':
                recursived = True
                swap.append(flip())
            else:
                swap.append(target)
    except StopIteration:
        pass

    # x1234 -> x3412로 되도록 순서변경해준다
    swap[1], swap[2], swap[3], swap[4] = swap[3], swap[4], swap[1], swap[2]
    return ''.join(swap)


if __name__ == '__main__':
    for case in range(int(input())):
        string = iter(input())
        print(flip())
