# 8.2 wildcard
# * = 0글자 이상
# ? = 1글자
# 패턴과 패턴으로 검색할 수 있는 대상들이 주어지고 그 대상중 맞는 것만 반환
# 입력 C <= 10, 패턴, 대상들 <=50
# 패턴 = 알파벳, 대소문자, 숫자, *, ?
# 파일명 알파벳, 대소문자, 숫자, 문자열길이 <=100, 공백미포함
def search(pattern, file):
    idx = 0
    while idx < len(pattern) and idx < len(file) and (pattern[idx] == '?' or pattern[idx] == file[idx]):
        idx += 1

    # 종료됨, 종료된 사유에 따라서 로직을 처리
    if idx == len(pattern):
        return idx == len(file)

    if pattern[idx] == '*':
        for i in range(len(file)-idx+1):
            if search(pattern[idx+1:], file[idx+i:]):
                return True
    return False

if __name__ == '__main__':
    pattern = 'he?p'
    file = 'help'
    assert search(pattern, file)
    file = 'heap'
    assert search(pattern, file)
    file = 'helpp'
    assert not search(pattern, file)

    pattern = '*p*'
    file = 'help'
    assert search(pattern, file)
    file = 'papa'
    assert search(pattern, file)
    file = 'hello'
    assert search(pattern, file)

    # for _ in range(int(input())):
    #     pattern = input()
    #     ret = []
    #     for f in range(int(input())):
    #         file = input()
    #         if search(pattern, file):
    #             ret.append(file)
    #     ret.sort()
    #     print(ret)
