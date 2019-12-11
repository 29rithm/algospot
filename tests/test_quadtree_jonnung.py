from QUADTREE.quadtree_jonnung import split_squad, change_up_down


def test__문자열에_w와_b로_분류해서_각각을_요소로_갖는_리스트를_만든다():
    case1 = "w"
    case2 = "xwbbb"

    expected_result1 = "w"
    expected_result2 = ["w", "b", "b", "b"]

    result1 = split_squad(iter(case1))
    result2 = split_squad(iter(case2))

    assert result1 == expected_result1
    assert result2 == expected_result2


def test__문자열이_x로_시작하면_다음에_나오는_문자들은_길이가_4인_리스트에_담긴다():
    case1 = "xwbxwbwbw"
    case2 = "xxwwwbxwxwbbbwwxxxwwbbbwwwwbb"

    expected_result1 = ["w", "b", ["w", "b", "w", "b"], "w"]
    expected_result2 = [["w", "w", "w", "b"], ["w", ["w", "b", "b" ,"b"], "w", "w"], [[["w", "w", "b", "b"], "b", "w", "w"], "w", "w", "b"], "b"]

    result1 = split_squad(iter(case1))
    result2 = split_squad(iter(case2))

    assert result1 == expected_result1
    assert result2 == expected_result2


def test__분해된_리스트에서_첫번째두번째와_세번째네번째_순서를_바꿔_결합한_문자열을_반환한다():
    case0 = ["b"]
    case1 = ["w", "b", "b", "b"]
    case2 = ["b", "w", ["w", "b", "b", "w"], "b"]
    case3 = [["w", "w", "w", "b"], ["w", ["w", "b", "b" ,"b"], "w", "w"], [[["w", "w", "b", "b"], "b", "w", "w"], "w", "w", "b"], "b"]

    expected_result0 = "b"
    expected_result1 = "xbbwb"
    expected_result2 = "xxbwwbbbw"
    expected_result3 = "xxwbxwwxbbwwbwbxwbwwxwwwxbbwb"

    result0 = change_up_down(case0)
    result1 = change_up_down(case1)
    result2 = change_up_down(case2)
    result3 = change_up_down(case3)

    assert result0 == expected_result0
    assert result1 == expected_result1
    assert result2 == expected_result2
    assert result3 == expected_result3
