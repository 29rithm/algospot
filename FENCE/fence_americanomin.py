def get_width_block(index, fence):
    right_index = index + 1
    left_index = index - 1
    left_block = 0
    right_block = 0
    while True:
        if right_index > len(fence) - 1:
            break

        if fence[index] <= fence[right_index]:
            right_index += 1
            right_block += 1
        else:
            break

    while True:
        if left_index < 0:
            break

        if fence[index] <= fence[left_index]:
            left_index -= 1
            left_block += 1
        else:
            break

    return right_block, left_block


def get_max_square_measure(fence):
    max_square_measure = 0
    calculated_height = {}

    for i, i_height in enumerate(fence):
        calculated_square_measure = calculated_height.get(i_height)

        if (
            calculated_square_measure
            and i > 0
            and i in range(*calculated_square_measure)
        ):
            continue

        right_block, left_block = get_width_block(i, fence)

        square_measure = i_height * (1 + right_block + left_block)
        calculated_height[i_height] = [i - left_block, i + right_block]

        if square_measure > max_square_measure:
            max_square_measure = square_measure

    return max_square_measure


if __name__ == "__main__":
    tc = input()
    result_list = []
    for i in range(int(tc)):
        width = int(input())
        fence = [int(height) for height in input().split(" ")]
        result_list.append(get_max_square_measure(fence))

    for result in result_list:
        print(result)
