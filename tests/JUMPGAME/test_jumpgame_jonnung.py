import pytest

from JUMPGAME.jumpgame_jonnung import JumpGame


@pytest.fixture
def case1():
    return [
        [1, 1],
        [1, 0],
    ]


@pytest.fixture
def case2():
    return [
        [1, 1, 2],
        [1, 2, 3],
        [2, 4, 0],
    ]


@pytest.fixture
def case3():
    return [
        [2, 5, 1, 6, 1, 4, 1],
        [6, 1, 1, 2, 2, 9, 3],
        [7, 2, 3, 2, 1, 3, 1],
        [1, 1, 3, 1, 7, 1, 2],
        [4, 1, 2, 3, 4, 1, 2],
        [3, 3, 1, 2, 3, 4, 1],
        [1, 5, 2, 9, 4, 7, 0],
    ]


@pytest.fixture
def case4():
    return [
        [2, 5, 1, 6, 1, 4, 1],
        [6, 1, 1, 2, 2, 9, 3],
        [7, 2, 3, 2, 1, 3, 1],
        [1, 1, 3, 1, 7, 1, 2],
        [4, 1, 2, 3, 4, 1, 3],
        [3, 3, 1, 2, 3, 4, 1],
        [1, 5, 2, 9, 4, 7, 0],
    ]


def test__주어진_위치에서_오른쪽_아래쪽으로_이동할_수_있는지_확인(case1):
    jg1 = JumpGame(2, case1)
    jg2 = JumpGame(2, case1)

    jg1_down, jg1_right = jg1.check_movable(0, 0)
    jg2_down, jg2_right = jg2.check_movable(0, 1)

    assert jg1_down is True
    assert jg1_right is True
    assert jg2_down is True
    assert jg2_right is False


def test__주어진_위치에서_오른쪽으로_이동_했을때_값을_알수있다(case2):
    jg = JumpGame(3, case2)
    position, distance = jg.right(0, 0)
    assert position == (0, 1)
    assert distance == 1


def test__오른쪽으로_이동_했을때_좌표가_최종_목적지이면_참(case2):
    jg = JumpGame(3, case2)
    position, distance = jg.right(2, 0)
    assert position == (2, 2)
    assert distance == 0


def test__끝까지_갈_수_있는_방법이_존재한다(case2, case3):
    jg1 = JumpGame(3, case2)
    jg1.jump()
    assert jg1.reachable is True

    jg2 = JumpGame(7, case3)
    jg2.jump()
    assert jg2.reachable is True

def test__끝까지_갈_수_있는_방법이_존재하지_않는다(case4):
    jg3 = JumpGame(7, case4)
    jg3.jump()
    assert jg3.reachable is False