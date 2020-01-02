# * 이 문제가 된다
# so*me*bo*dy
# so* me* bo* dy
# 이렇게 네 개로 쪼개버리고
# * 을 만났을 때 부분문제로 처리한다
# ab fg
# ab cdefg

def check_match(pattern, string):
    idx = 0
    while idx < len(pattern) and idx < len(string) and ((pattern[idx] == string[idx]) or pattern[idx] == '?'):
        idx += 1

    if idx == len(pattern):
        return idx == len(string)

    if pattern[idx] == '*':
        for i in range(len(string)-idx+1):
            if(check_match(pattern[idx+1:], string[idx+i:])):
                return True
    return False

if __name__ == '__main__':
    for _ in range(int(input())):
        pattern = input()
        for case in range(int(input())):
            string = input()
            result = check_match(pattern, string)
            if result:
                print(string)

# if __name__ == '__main__':
#     assert check_match('he?p', 'help')
#     assert check_match('?e?p', 'help')
#     assert not check_match('he?p', 'helpp')
#     assert check_match('*p', 'help')
#     assert check_match('h*', 'help')
#     assert check_match('h*p', 'help')
#     assert check_match('*l*', 'help')
#     assert check_match('*p*', 'help')
#     assert check_match('*p*', 'papa')
#     assert not check_match('*p*', 'hello')

