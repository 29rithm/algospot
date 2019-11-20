
input_text = None


def solution(input1, input2):
    nm = input1.split(' ')
    data = input2.split(' ')

    if int(nm[1]) == 0:
        return 0

    q = [set(data[count * 2:count * 2 + 2]) for count in range(int(nm[1]))]

    def memorial(position):
        memory = [q[position]]

        if position == 0:
            return memory
        else:
            prior = memorial(position - 1)
            memory.extend([element for element in
                           [x.union(q[position]) for x in prior if len(x.intersection(q[position])) == 0] if
                           len(element) % 2 == 0])
            memory.extend(prior)
            return memory

    return len([case for case in memorial(len(q) - 1) if len(case) == int(nm[0])])


if not input_text:
    import sys
    test_case_count = sys.stdin.readline()

    for i in range(int(test_case_count)):
        first_line = input().rstrip().lstrip()
        second_line = input().rstrip().lstrip()

        print(solution(input1=first_line, input2=second_line))
else:
    input_data = input_text.split('\n')

    for i in range(int(input_data[0])):
        first_line = input_data[(i+1)*2-1].rstrip().lstrip()
        second_line = input_data[(i+1)*2].rstrip().lstrip()

        print(solution(input1=first_line, input2=second_line))
