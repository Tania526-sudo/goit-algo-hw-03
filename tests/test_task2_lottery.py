from src.goit_algo_hw_03.task2_lottery import get_numbers_ticket


def test_valid_range():
    nums = get_numbers_ticket(1, 49, 6)
    assert len(nums) == 6
    assert all(1 <= n <= 49 for n in nums)
    assert nums == sorted(nums)
    assert len(nums) == len(set(nums))


def test_invalid_range():
    assert get_numbers_ticket(10, 5, 3) == []


def test_invalid_quantity():
    assert get_numbers_ticket(1, 10, 20) == []
