max_size = -1

def counter(fences):
    global max_size
    # if len(fences) == 1:
    #     max_size = fences[0] if fences[0] > max_size else max_size
    #     return
    if len(fences) < 2:
        return
    mid = len(fences)//2
    # 중간을 걸쳐서 있다고 가정
    left_size = -1
    left = -1
    right = -1

    for i in range(0, mid):
        target = fences[i:mid]
        subsize = min(target) * len(target)
        if subsize > left_size:
            left_size = subsize
            left = i
    left_size = min(fences[0:mid]) * len(fences[0:mid])
    right_size = -1
    for j in range(mid, len(fences)):
        target = fences[mid:j+1]
        subsize = min(target) * len(target)
        if subsize > right_size:
            right_size = subsize
            right = j

    mid_size = -1
    if left> -1 and right > -1:
        target = fences[left:right+1]
        mid_size = min(target) * len(target)

    # 중간에 걸치지 않았다고 가정
    if mid_size > left_size and mid_size > right_size:
        max_size = mid_size
        # print("left", left, "right", right, "max", max_size, "fences", fences)
        return
    elif left_size > right_size:
        max_size = left_size if left_size > max_size else max_size
        return
        # print("left", left, "right", right, "max", max_size, "fences", fences)
        # counter(fences[0:mid])
    else:
        max_size = right_size if right_size > max_size else max_size
        return
        # print("left", left, "right", right, "max", max_size, "fences", fences)
        # counter(fences[mid:])


if __name__ == '__main__':
    # for c in range(int(input())):
    #     max_size = -1
    #     fence_count = int(input())
    #     counter([int(i) for i in input().split()])
    #     print(max_size)
    max_size = -1
    counter([7,1,5,9,6,7,3])
    assert max_size == 20
    print("===========")
    max_size = -1
    counter([1,4,4,4,4,1,1])
    assert max_size == 16
    print("===========")
    max_size = -1
    counter([1,8,2,2])
    assert max_size == 8
