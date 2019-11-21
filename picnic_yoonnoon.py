def solution(input1, input2):
    nm = input1.split(' ')
    data = input2.split(' ')

    if int(nm[1]) == 0:
        return 0

    q = [set(data[count * 2:count * 2 + 2]) for count in range(int(nm[1]))]

    def get_accumulated_data(position):
        memo = [q[position]]

        if position == 0:
            return memo
        else:
            prior = get_accumulated_data(position - 1)
            memo.extend([element for element in
                        [x.union(q[position]) for x in prior if len(x.intersection(q[position])) == 0] if
                        len(element) % 2 == 0])
            memo.extend(prior)
            return memo

    return len([case for case in get_accumulated_data(len(q) - 1) if len(case) == int(nm[0])])


test_case_count = input().rstrip().lstrip()
for i in range(int(test_case_count)):
    first_line = input().rstrip().lstrip()
    second_line = input().rstrip().lstrip()

    print(solution(input1=first_line, input2=second_line))
