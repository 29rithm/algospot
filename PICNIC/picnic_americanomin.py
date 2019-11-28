import copy
import sys


def populate_pairs(student_list, relation_set):
    if len(student_list) < 1:
        return []

    total_friend_pairs = []
    copied_student_list = copy.deepcopy(student_list)
    first_student = copied_student_list.pop()

    for copied_student in copied_student_list:
        if first_student>copied_student:
            one_pair = f"{copied_student}:{first_student}"
        else:
            one_pair = f"{first_student}:{copied_student}"

        if not one_pair in relation_set:
            continue

        nested_student_list = copy.deepcopy(copied_student_list)
        nested_student_list.remove(copied_student)
        combinations = populate_pairs(nested_student_list, relation_set)

        if combinations:
            for combination in combinations:
                combination.add(one_pair)
                total_friend_pairs.append(combination)
        else:
            data = set()
            data.add(one_pair)
            total_friend_pairs.append(data)

    return total_friend_pairs


def picnic(friends_meta_info, friends_relations):
    friends_meta_info = [ meta for meta in friends_meta_info.split(' ') if meta]
    friends_relations = [ relation for relation in friends_relations.split(' ') if relation]
    relation_set = set()

    for i, student in enumerate(friends_relations):
        if i % 2 != 0 or len(friends_relations) - 1 == i:
            continue
        key_element = friends_relations[i:i + 2]
        key_element.sort()
        relation_key = ':'.join(key_element)
        relation_set.add(relation_key)

    friends_count = int(friends_meta_info[0])
    friends_count = int(friends_meta_info[0])

    student_list = [a for a in range(friends_count)]
    pairs = populate_pairs(student_list, relation_set)

    return pairs

if __name__ == '__main__':
    rl = lambda : sys.stdin.readline()
    test_case_count = int(rl())

    result = []
    for i in range(test_case_count):
        first_line = rl().rstrip().lstrip()
        second_line = rl().rstrip().lstrip()
        print(len(picnic(first_line, second_line)))
