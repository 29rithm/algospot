from LIS.lis_jonnung import lis_solution


def test_lis_solution():
    tc1 = [1, 2, 3, 4]
    tc2 = [5, 4, 3, 2, 1, 6, 7, 8]
    tc3 = [5, 6, 7, 8, 1, 2, 3, 4]

    assert lis_solution(tc1) == 4
    assert lis_solution(tc2) == 4
    assert lis_solution(tc3) == 4