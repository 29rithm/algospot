def get_max_square_measure(fence):
    max_square_measure = 0
    width = len(fence)

    for i in range(width):
        height = fence[i]

        max_vertical_rectangle_height = height
        max_vertical_rectangle_width = 1
        max_horizontal_rectangle_height = height
        max_horizontal_rectangle_width = 1

        for j in range(i + 1, width):
            next_height = fence[j]
            if height <= next_height:
                max_vertical_rectangle_width += 1
            else:
                break

        for j in range(i + 1, width):
            next_height = fence[j]
            if max_horizontal_rectangle_height > next_height:
                max_horizontal_rectangle_height = next_height
            else:
                break
            max_horizontal_rectangle_width += 1

        verical_squared_measure = (
            max_vertical_rectangle_height * max_vertical_rectangle_width
        )
        horizontal_squared_measure = (
            max_horizontal_rectangle_height * max_horizontal_rectangle_width
        )

        if verical_squared_measure > max_square_measure:
            max_square_measure = verical_squared_measure

        if horizontal_squared_measure > max_square_measure:
            max_square_measure = horizontal_squared_measure

    return max_square_measure


if __name__ == "__main__":
    tc = input()

    for i in range(int(tc)):
        width = int(input())
        fence = [int(height) for height in input().split(" ")]
        result = get_max_square_measure(width, fence)
        print(result)
