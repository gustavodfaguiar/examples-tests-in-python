import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    '''
    Examples:    
      - The sum of 2 and 2 returns 4
      - When summing 2 and 2 it must return 4
      - Given two positive numbers when sum then four is expected
    '''
    def test_given_two_positive_numbers_the_sum_is_four(self):
        expected = 4
        result_sum = Calculator().sum(2, 2)
        self.assertEqual(result_sum, expected)
   
    '''
    Example:
       - Given the sum of -2 and -3, the result must be -5
    '''
    def test_given_two_negative_numbers_the_sum_is_minus_five(self):
        expected = -5
        result_sum = Calculator().sum(-2, -3)
        self.assertEqual(result_sum, expected)

    def test_given_the_sum_of_two_strings_it_expected_an_exception(self):
        expected = "Two integer values are expected"
        with self.assertRaises(Exception) as context:
            Calculator().sum('2', '2')
            
        self.assertTrue(expected in str(context.exception))


if __name__ == '__main__':
    unittest.main()
