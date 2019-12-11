def split_squad(compressed_str_iter):
    ret = []
    while True:
        try:
            char = next(compressed_str_iter)
            if char == "x":
                ret.append(split_squad(compressed_str_iter))
            else:
                ret.append(char)

            if len(ret) == 4:
                return ret
        except StopIteration:
            return ret[0]


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
