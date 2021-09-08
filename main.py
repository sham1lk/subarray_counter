import unittest
from random import randint


def even_subarray(numbers, k):
    """
    :param numbers: list of integers
    :param k: int, max number of odd elements in subarray
    :return: number of subarrays
    """
    count = 0
    odd_num = 0
    dp = [0 for i in range(len(numbers)+1)]

    for i in range(len(numbers)):
        dp[odd_num] += 1

        # if array element is odd
        if numbers[i] % 2:
            odd_num += 1

        for j in range(min(odd_num, k) + 1):
            count += dp[odd_num - j]

    return count


class TestEvenSubarray(unittest.TestCase):
    """
    Test even_subarray function
    """

    def test_all_even(self):
        """
        All even test case.
        The answer should be all combinations of all sizes
        """
        for p in range(100):
            size_of_arr = randint(1, 10000)
            arr = [0 for i in range(size_of_arr)]
            ans = 0
            for i in range(size_of_arr):
                ans += size_of_arr - i
            self.assertEqual(even_subarray(arr, 0), ans)

    def test_all_odd(self):
        """
        All odd test case.
        The answer should be all combination of all sizes smaller then k
        """
        for p in range(100):
            k = randint(0, 10)
            size_of_arr = randint(10, 10000)
            arr = [1 for i in range(size_of_arr)]
            ans = 0
            for i in range(k):
                ans += size_of_arr - i
            self.assertEqual(even_subarray(arr, k), ans)

    def test_some_cases(self):
        tests = [([6, 3, 5, 8], 1, 6),
                 ([2, 3, 3, 2, 2, 3, 2, 2, 2, 2], 3, 55)]
        for t in tests:
            self.assertEqual(even_subarray(t[0], t[1]), t[2])


if __name__ == '__main__':
    unittest.main()
