import re

def check_wildcard(wildcard_regex, search_text_list):
    cleaned_regex = wildcard_regex.replace('?', '.')
    cleaned_regex = cleaned_regex.replace('*', '.*')
    regrex = re.compile(cleaned_regex)

    confimed_text_list = []

    for search_text in search_text_list:
        matched_data = regrex.findall(search_text)

        if matched_data and len(matched_data[0]) == len(search_text):
            confimed_text_list.append(search_text)

    confimed_text_list.sort()
    return confimed_text_list


if __name__ == "__main__":
    for problem_count in range(int(input())):
        board = []
        blocked = []
        wildcard_regex = input().strip()
        target_text_count = int(input())

        target_text_list = [input() for _ in range(target_text_count)]
        results = check_wildcard(wildcard_regex, target_text_list)

        for result in results:
            print(result)
