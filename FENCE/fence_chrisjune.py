def counter(fences):
    if len(fences) == 1:
        return fences[0]

    mid = len(fences)//2

    left = mid-1
    right = mid
    height = min(fences[left], fences[right])
    size = height * 2
    while 0 < left or right < len(fences)-1:
        if right < len(fences)-1 and (left==0 or fences[left-1] < fences[right+1]):
            right+=1
            height = min(height, fences[right])
        else:
            left-=1
            height = min(height, fences[left])
        size = max(size, height * (right-left+1))
    mid_size = size

    single = max(counter(fences[:mid]), counter(fences[mid:]))
    return max(mid_size, single)

if __name__ == '__main__':
    for c in range(int(input())):
        fence_count = int(input())
        print(counter([int(i) for i in input().split()]))