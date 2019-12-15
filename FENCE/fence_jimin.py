def get_max_square_measure(fence):
    max_square_measure = 0
    width = len(fence)

    for i in range(width):
        height = fence[i]

        start_width_index = i
        end_width_index = i

        for j in range(width):
            if height <= fence[j]:
                if j <= i:
                    start_width_index = j
                else:
                    end_width_index = j
            else:
                if j < i:
                    start_width_index = i
                else:
                    break

        verical_squared_measure = height * (( end_width_index-start_width_index)+1)

        if verical_squared_measure > max_square_measure:
            max_square_measure = verical_squared_measure

    return max_square_measure


if __name__ == "__main__":
    tc = input()

    for i in range(int(tc)):
        width = int(input())
        fence = [int(height) for height in input().split(" ")]
        result = get_max_square_measure(fence)
        print(result)
