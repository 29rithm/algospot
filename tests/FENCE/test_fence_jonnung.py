from FENCE.fence_jonnung import calculate_rectangle_size


def test__현재_위치_양옆으로_현재_높이보다_작을때까지_너비를_계산한다():
    # arrange
    fence1 = [1, 4, 4, 4, 4, 1, 1]
    rectangle_size1 = calculate_rectangle_size(len(fence1), fence1)

    fence2 = [7, 1, 5, 9, 6, 7, 3]
    rectangle_size2 = calculate_rectangle_size(len(fence2), fence2)

    fence3 = [1, 8, 2, 2]
    rectangle_size3 = calculate_rectangle_size(len(fence3), fence3)

    # assert
    assert rectangle_size1 == 16
    assert rectangle_size2 == 20
    assert rectangle_size3 == 8
