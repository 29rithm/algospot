"""
주어진 공간을 항상 4개로 분할 / 재귀적으로 표현
2^n x 2^n 크기

- 모든 픽셀이 검은색이면 크기와 상관없이 b
- 모든 픽셀이 흰색이면 크기와 상관없이 w
- 모든 색이 아니라면, 가로 세로 각각 2등분해 4개의 조각으로 쪼갬.
  x(왼쪽 위 부분의 압축 결과)(오른쪽 위 부분의 압축 결과)(왼쪽 아래 부분의 압축 결과)(오른쪽 아래 부분의 압축 결과)가 됩니다.
  예를 들어 그림 (a)의 왼쪽 위 4분면은 xwwwb로 압축됩니다.

주어진 문재를 상하 뒤집어서 다시 출력
주어지는 문자열은 1000개 이하
"""

"""
0<= N < 20
만약 N이 4면 
2^4 x 2^4 = 16 x 16 행렬.
1. 16 X 16 행렬을 가로, 세로 나눠 크기가 8 x 8 인 사사분면으로 만듦
2. 위에서 만든 사사분면에서 w(모두 흰색), b(모두 검정), x(흰색, 검정 혼합)을 셈
3. x인 부분을 찾아 가로, 세로로 나눠 크기가 4 x 4인 사사분면으로 만듦
4. 위에서 만든 사사분면에서 w(모두 흰색), b(모두 검정), x(흰색, 검정 혼합)을 셈
5. x인 부분을 찾아 가로, 세로로 나눠 크기가 2 x 2인 사사분면으로 만듦
6. 위에서 만든 사사분면에서 w(모두 흰색), b(모두 검정), x(흰색, 검정 혼합)을 셈
7. x인 부분을 찾아 가로, 세로로 나눠 크기가 1 x 1인 사사분면으로 만듦
8. 위에서 만든 사사분면에서 w(모두 흰색), b(모두 검정)을 셈
8-1. 여기서는 1 x 1이기 때문에 x(흰색, 검정 혼합)가 나올 수 없음


그래프의 탐색 순서는 VLR (preorder)
루트노드는 x 고정

상하 뒤집는 건 모든 사사분면에 적용

쿼드트리 구성 후, 상하 반전된 걸 읽는 순서는 3,4,1,2 

받은 문자열 중 첫 번째 x는 생략 (루트노드)

들어온 데이터는 아래와 같이 꾸민다.
xwbbw:
[w,b,b,w]

상하 뒤집으면 3,4,1,2 순으로 읽어서 아래와 같이 쓴다.
[b,w,w,b]

xbwxwbbwb:
[b,w,(x,(w,b,b,w)),b]
상하 뒤집으면 3,4,1,2 순으로 읽어서 아래와 같이 쓴다.
[(x,(b,w,w,b)),b,b,w]

pseudo code

# 함수 make(i):
# t = s[i]
# if t == 'x':
#     pass
# 
# origin.append(t)

함수 make(s):
    (x,(s))

# 주어진 값을 먼저 위 형식으로 만든다.

origin = []

is_inner = False
a = ('x',())
for s in 원본데이터:
    if is_inner:
        make(s)
    elif s != 'x' and not is_inner:
        origin.append(s)
    else:
        is_inner = True
        
        

# 트리를 구현해서??
class Tree:
    
    r = [[],[],[],[]]


"""


def read(r, i):
    if i == 5:
        return
    target = r[orders[i]]
    if isinstance(target, list):
        read(target, 0)
    else:
        result.append(target)
    read(r, i + 1)


if __name__ == '__main__':
    orders = [0, 3, 4, 1, 2]
    for _ in range(int(input())):
        tc = input()
        result = []
        tree = []

        if len(tc) == 1:
            print(tc)
            continue

        # 뒤에서 부터 세주면서 subtree를 구성
        # 루트 노드는 빼고 세야 쿼드트리 형태를 이룰 수 있음
        for i in range(len(tc) - 1, 0, -1):
            node = tc[i]
            if node != 'x':
                tree.append(node)
                continue
            # 쿼드트리이므로 들어온 순으로 4개를 뽑아서 tree를 구성해줌
            subtree = tree[-1:-5:-1]
            # 부모 노드인 x를 붙여줌
            subtree.insert(0, node)
            del tree[-1:-5:-1]
            tree.append(subtree)
        # 루트노드를 제외하고 최하단 리프노드부터 세었으므로 가장 마지막에 루트노드인 x를 추가
        tree.append('x')
        tree.reverse()

        read(tree, 0)
        print(''.join(result))
