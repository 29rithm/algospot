def lis(subsequence):
    if not subsequence:
        return print(len(blank))
    if len(subsequence) == 1:
        if blank:
            if blank[-1] < subsequence[0]:
                blank.append(subsequence[0])
    elif(subsequence[0] < subsequence[1]):
        if not blank:
            blank.append(subsequence[1])
    subsequence.pop()
    lis(subsequence)
if __name__ == '__main__':
    import sys
    test_case = sys.stdin.readline()
    for tc in range(int(test_case)):
        blank = []
        num = input()
        subsequence = input().split(' ')
        case_list = [int(i) for i in subsequence]
        print(lis(case_list))
