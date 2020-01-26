# 8.2 wildcard
# * = 0글자 이상
# ? = 1글자
# 패턴과 패턴으로 검색할 수 있는 대상들이 주어지고 그 대상중 맞는 것만 반환
# 입력 C <= 10, 패턴, 대상들 <=50
# 패턴 = 알파벳, 대소문자, 숫자, *, ?
# 파일명 알파벳, 대소문자, 숫자, 문자열길이 <=100, 공백미포함

def search(pattern, file):
    p_iter = iter(pattern)
    f_iter = iter(file)
    while True:
        p = next(p_iter, None)
        f = next(f_iter, None)

        if not p and not f:
            break

        # * 로 stack에서 빠져나올떄 인덱스를 확인할 마크
        mark_idx = -1
        if p == f or p == '?':
            continue
        if not p or not f:
            return False
    return True


if __name__ == '__main__':
    pattern = 'he?p'
    file = 'help'
    assert search(pattern, file)
    file = 'heap'
    assert search(pattern, file)
    file = 'helpp'
    assert not search(pattern, file)
    # for _ in range(int(input())):
    #     pattern = input()
    #     ret = []
    #     for f in range(int(input())):
    #         file = input()
    #         if search(pattern, file):
    #             ret.append(file)
    #     ret.sort()
    #     print(ret)

