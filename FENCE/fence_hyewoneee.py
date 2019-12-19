def Fence(fence_list):
    max_rectangle = 0

    for i in range(len(fence_list)):
        height = fence_list[i]
        rectangle = height
        for j in range(i-1, -1, -1):
            if height <= fence_list[j]:
                rectangle += height
            else:
                break
        for j in range(i+1, len(fence_list)):
            if height <= fence_list[j]:
                rectangle += height
            else:
                break
        if max_rectangle < rectangle:
            max_rectangle = rectangle
    return max_rectangle

if __name__ == '__main__':
    import sys
    case = sys.stdin.readline()

    if int(case) > 50:
        raise print('테스트 케이스는 50번을 넘길 수 없다.')

    for tc in range(int(case)):
        max_height = 0
        fence_num = input()
        height = input().split(' ')
        print(Fence([int(i) for i in height]))
