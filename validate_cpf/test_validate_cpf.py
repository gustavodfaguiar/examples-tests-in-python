import unittest
from validate_cpf import validate_cpf


class TestValidateCpf(unittest.TestCase):
    def test_given_cpf_valid_the_return_is_true(self):
        result = validate_cpf('529.982.247-25')
        self.assertTrue(result)

    def test_given_cpf_invalid_the_return_is_false(self):
        result = validate_cpf('529.982.247-21')
        expected = False
        self.assertEqual(result, expected)
    
    def test_given_cpf_with_the_wrong_formatting_the_return_is_false(self):
        result = validate_cpf('529.982.247/25')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
