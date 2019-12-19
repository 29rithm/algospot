from FENCE.fence_americanomin import get_max_square_measure


def test__get_max_square_measure_case_1():
    fence = [7, 1, 5, 9, 6, 7, 3]
    assert 20 == get_max_square_measure(fence)


def test__get_max_square_measure_case_2():
    fence = [1, 4, 4, 4, 4, 1, 1]
    assert 16 == get_max_square_measure(fence)


def test__get_max_square_measure_case_3():
    fence = [1, 8, 2, 2]
    assert 8 == get_max_square_measure(fence)


def test__get_max_square_measure_case_4():
    fence = [2, 2]
    assert 4 == get_max_square_measure(fence)


def test__get_max_square_measure_case_5():
    fence = [1, 3]
    assert 3 == get_max_square_measure(fence)


def test__get_max_square_measure_case_6():
    fence = [1, 4, 1, 5, 4, 4, 4]
    assert 16 == get_max_square_measure(fence)
