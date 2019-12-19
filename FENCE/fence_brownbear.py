"""
연속된 판자를 자르는데 가장 큰 넓이를 가진 직사각형의 크기를 구하기
- 각 판자의 넓이는 1 고정

C: tc 반복횟수 , N:  판자의 수, H: 판자의 높이


7
7 1 5 9 6 7 3

20

7
1 4 4 4 4 1 1

16

4
1 8 2 2

8
"""
"""
1 <= N <= 20000
0 <= H <= 10000

판자의 수가 20000개이므로 재귀로 푼다면 스택오버플로우가 날 가능성이 있음
만약 nested loop이 발생했을 때, 20000 * 10000의 케이스에서 3초가 넘을 수 있음
- 로컬에서 테스트 했을 때, for 20000 * 10000 진행 시 약 16초 소요

정렬해서 풀 수가 없음

7 : 7
1 : 7
5 : 7
9 : 10
6 : 15
7 : 20
3 : 20 
> 20


"""


# 시간초과
# def run(left, right):
#     if left == right:
#         return h[left]
#     mid = (left + right) // 2
#     ret = max(run(left, mid), run(mid+1, right))
#
#     lower, higher = mid, mid + 1
#     height = min(h[lower], h[higher])
#     ret = max(ret, height * 2)
#
# while left < lower or higher < right:
#     if higher < right and (lower == left or h[higher + 1] > h[lower - 1]):
#         higher += 1
#         height = min(height, h[higher])
#     else:
#         lower -= 1
#         height = min(height, h[lower])
#     ret = max(ret, height * (higher - lower + 1))
#     return com(height, ret, left, lower, higher, right)
#
# def com(height, ret, left, lower, higher, right):
#     if not (left < lower or higher < right):
#         return ret
#     if higher < right and (lower == left or h[higher + 1] > h[lower - 1]):
#         higher += 1
#         height = min(height, h[higher])
#     else:
#         lower -= 1
#         height = min(height, h[lower])
#     ret = max(ret, height * (higher - lower + 1))
#     return com(height, ret, left, lower, higher, right)
#
#


#
# def run(fences, n):
#     def inner(max_area, new_index):
#         while stack and stack[-1][1] >= fence:
#             max_area = max(max_area, stack[-1][1] * (i - stack[-1][0]))
#             new_index = stack.pop()[0]
#         return (max_area, new_index)
#
#     max_area = 0
#     stack = []
#     for i, fence in enumerate(fences):
#         max_area, range_i = inner(max_area, i)
#         stack.append((range_i, fence))
#
#     max_area, new_index = inner(max_area, n)
#     return max_area
#
#
# if __name__ == '__main__':
#     test_case = 1
#     for case in range(test_case):
#         n = 7
#         fences = list(map(int, '7 1 5 9 6 7 3'.split(' ')))
#         print(run(fences, n))


# 시간초과
# def run(left, right):
#     if left == right:
#         return h[left]
#     mid = (left + right) // 2
#     ret = max(run(left, mid), run(mid+1, right))
#
#     lower, higher = mid, mid + 1
#     height = min(h[lower], h[higher])
#     ret = max(ret, height * 2)
#     while left < lower or higher < right:
#         if higher < right and (lower == left or h[higher + 1] > h[lower - 1]):
#             higher += 1
#             height = min(height, h[higher])
#         else:
#             lower -= 1
#             height = min(height, h[lower])
#         ret = max(ret, height * (higher - lower + 1))
#
#     return ret
#
# for i in range(int(input())):
#     n = int(input())
#     h = list(map(int, input().split()))
#     print(run(0, n-1))


def run():
    def inner(area, index):
        while stack and stack[-1][1] >= fence:
            area = max(area, stack[-1][1] * (i - stack[-1][0]))
            index = stack.pop()[0]
        return area, index

    max_area = 0
    stack = []
    for i, fence in enumerate(fences):
        max_area, rear = inner(max_area, i)
        stack.append((rear, fence))

    return max_area


if __name__ == '__main__':
    for case in range(int(input())):
        n = int(input())
    fences = list(map(int, input().split(' ')))
    fences.append(0)
    print(run())
