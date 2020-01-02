def wild_card(pattern, name_list):
    import re
    result = []
    mark_pattern = pattern.replace('?', '.')
    reg_pattern = mark_pattern.replace('*', '.*')
    reg_pattern += '$'
    re = re.compile(reg_pattern)
    for s in name_list:
        match = re.match(s)
        if match:
            result.append(match.group())
    result.sort()
    return '\n'.join(result)

if __name__ == '__main__':
    import sys
    test_case = sys.stdin.readline()

    for tc in range(int(test_case)):
        pattern = input()
        name_count = input()
        name_list = []
        for nc in range(int(name_count)):
            name_list.append(input())
        print(wild_card(pattern, name_list))

