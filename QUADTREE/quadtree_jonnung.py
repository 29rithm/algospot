def split_squad(compress_str):
    if compress_str[0] == "x":
        quad_str = compress_str[1:]
        temp = []
        for i, v in enumerate(quad_str):
            if v == "x":
                temp.append(split_squad(quad_str[i:]))
            else:
                temp.append(v)

            if len(temp) == 4:
                return temp
        return temp

    else:
        return [compress_str]


def change_up_down(decompress_list):
    if len(decompress_list) == 1:
        return decompress_list[0]

    copied_decompress_list = decompress_list[:]
    for i, v in enumerate(copied_decompress_list):
        if isinstance(v, list):
            copied_decompress_list[i] = change_up_down(v)

    decompress_list[0], decompress_list[1] = copied_decompress_list[2], copied_decompress_list[3]
    decompress_list[2], decompress_list[3] = copied_decompress_list[0], copied_decompress_list[1]

    return "x" + "".join(decompress_list)
